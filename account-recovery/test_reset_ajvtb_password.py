"""Password recovery tests; creates temporary databases only."""
from contextlib import redirect_stdout
import io
from pathlib import Path
import secrets
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from werkzeug.security import check_password_hash, generate_password_hash
import reset_ajvtb_password as reset


class PasswordResetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'etracker.db'
        self.old = secrets.token_urlsafe(20)
        self.new = secrets.token_urlsafe(20)
        with sqlite3.connect(self.path) as db:
            db.executescript('''CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT UNIQUE,
                role TEXT, password_hash TEXT); CREATE TABLE transactions(id INTEGER PRIMARY KEY, note TEXT);''')
            db.execute('INSERT INTO users VALUES (1,?,?,?)', ('AJVTB','chief',generate_password_hash(self.old)))
            db.execute('INSERT INTO users VALUES (2,?,?,?)', ('admin','admin','unchanged-other-hash'))
            db.execute("INSERT INTO transactions VALUES (1,'Original application')")

    def test_reset_backup_and_preservation(self):
        username, backup = reset.reset_password(self.path, self.new)
        self.assertEqual(username, 'AJVTB')
        with sqlite3.connect(self.path) as db:
            row = db.execute('SELECT username,role,password_hash FROM users WHERE id=1').fetchone()
            self.assertEqual(row[:2], ('AJVTB','chief'))
            self.assertTrue(check_password_hash(row[2],self.new))
            self.assertFalse(check_password_hash(row[2],self.old))
            self.assertEqual(db.execute('SELECT password_hash FROM users WHERE id=2').fetchone()[0], 'unchanged-other-hash')
            self.assertEqual(db.execute('SELECT * FROM transactions').fetchall(), [(1,'Original application')])
        with sqlite3.connect(backup) as db:
            self.assertTrue(check_password_hash(db.execute('SELECT password_hash FROM users WHERE id=1').fetchone()[0],self.old))
        self.assertNotIn(self.new,self.path.read_bytes().decode('latin1'))

    def test_missing_database_is_not_created(self):
        missing = self.path.parent/'missing.db'
        with self.assertRaises(ValueError):reset.reset_password(missing,self.new)
        self.assertFalse(missing.exists())

    def test_missing_ambiguous_or_wrong_role_is_rejected(self):
        for operation in ("DELETE FROM users WHERE id=1", "UPDATE users SET role='staff' WHERE id=1",
                          "INSERT INTO users VALUES (3,'ajvtb','chief','other-hash')"):
            with sqlite3.connect(self.path) as db:
                db.execute('DELETE FROM users WHERE id=3')
                db.execute("INSERT OR REPLACE INTO users VALUES (1,'AJVTB','chief','original-hash')")
                db.execute(operation)
                before=db.execute('SELECT * FROM users ORDER BY id').fetchall()
            with self.assertRaises(ValueError):reset.reset_password(self.path,self.new)
            with sqlite3.connect(self.path) as db:self.assertEqual(db.execute('SELECT * FROM users ORDER BY id').fetchall(),before)
        self.assertFalse((self.path.parent/'account-reset-backups').exists())

    def test_short_or_blank_password_is_rejected(self):
        for password in ('short', ' '*20):
            with self.assertRaises(ValueError):reset.reset_password(self.path,password)
        self.assertFalse((self.path.parent/'account-reset-backups').exists())

    def test_cli_mismatch_changes_nothing_and_does_not_print_password(self):
        output = io.StringIO()
        with patch('sys.argv',['reset_ajvtb_password.py','--database',str(self.path)]), \
                patch.object(reset.getpass,'getpass',side_effect=[self.new,self.old]), redirect_stdout(output):
            self.assertEqual(reset.main(),1)
        self.assertIn('Passwords do not match',output.getvalue())
        self.assertNotIn(self.new,output.getvalue())
        self.assertNotIn(self.old,output.getvalue())
        self.assertFalse((self.path.parent/'account-reset-backups').exists())


if __name__ == '__main__':
    unittest.main()
