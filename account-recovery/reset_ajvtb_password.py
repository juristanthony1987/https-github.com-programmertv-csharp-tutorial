"""Reset the existing AJVTB sign-in password in a local SQLite eTracker database."""
import argparse
import getpass
import os
from pathlib import Path
import sqlite3
import tempfile
import warnings
from datetime import datetime

from werkzeug.security import generate_password_hash


def open_database(path):
    path = Path(path).resolve()
    if not path.is_file():
        raise ValueError(f'Database not found: {path}. Put this tool beside app.py and etracker.db.')
    return sqlite3.connect(path.as_uri() + '?mode=rw', uri=True, timeout=10)


def find_account(db):
    rows = db.execute("SELECT id,username,role,password_hash FROM users WHERE lower(username)='ajvtb'").fetchall()
    if len(rows) != 1 or rows[0][2] != 'chief':
        raise ValueError('Expected one existing AJVTB account with the Chief role. No account was changed.')
    return rows[0]


def reset_password(path, password):
    if len(password) < 12 or not password.strip():
        raise ValueError('Use a password with at least 12 characters.')
    path = Path(path).resolve()
    db = open_database(path)
    try:
        original = find_account(db)
        new_hash = generate_password_hash(password)
        backup_dir = path.parent / 'account-reset-backups'
        backup_dir.mkdir(exist_ok=True, mode=0o700)
        descriptor, backup_name = tempfile.mkstemp(
            prefix=f'{path.stem}-before-AJVTB-reset-{datetime.now():%Y%m%d-%H%M%S}-',
            suffix='.db', dir=backup_dir)
        os.close(descriptor)
        backup = sqlite3.connect(backup_name)
        try:
            db.backup(backup)
        finally:
            backup.close()
        # Reject a competing account change after the backup was taken.
        with db:
            db.execute('BEGIN IMMEDIATE')
            if find_account(db) != original:
                raise ValueError('The account changed. Stop eTracker and run this tool again.')
            db.execute('UPDATE users SET password_hash=? WHERE id=?', (new_hash, original[0]))
        return original[1], Path(backup_name)
    finally:
        db.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', type=Path,
                        default=Path(os.environ.get('ETRACKER_DB', str(Path(__file__).resolve().parent / 'etracker.db'))))
    args = parser.parse_args()
    try:
        # Validate the selected database before asking for a password.
        db = open_database(args.database)
        try:
            username = find_account(db)[1]
        finally:
            db.close()
        print(f'Database: {args.database.resolve()}')
        print(f'Resetting the sign-in password for {username} (Chief).')
        print('Stop eTracker before continuing. An automatic database backup will be saved.')
        print('Enter a new password with at least 12 characters. Input is hidden.')
        with warnings.catch_warnings():
            warnings.simplefilter('error', getpass.GetPassWarning)
            password = getpass.getpass('New password: ')
            confirmation = getpass.getpass('Confirm new password: ')
        if password != confirmation:
            raise ValueError('Passwords do not match. No account was changed.')
        username, backup = reset_password(args.database, password)
        print(f'Success. Sign in as {username} using your new password.')
        print(f'Backup saved locally: {backup}')
        print('Restart eTracker. The separate Chief approval password is unchanged.')
        return 0
    except (ValueError, sqlite3.Error, OSError, getpass.GetPassWarning) as error:
        print(f'Reset failed: {error}')
        return 1
    except (EOFError, KeyboardInterrupt):
        print('\nReset cancelled. No account was changed.')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
