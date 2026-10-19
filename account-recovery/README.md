# Reset the AJVTB sign-in password

For the existing SQLite eTracker. Run this on the computer holding the active database.

1. Stop eTracker with Ctrl+C in its terminal.
2. Extract `etracker-ajvtb-reset.zip`. Copy `reset_ajvtb_password.py` and `RESET-AJVTB.bat` into the existing project folder, beside `app.py` and `etracker.db`.
3. Double-click `RESET-AJVTB.bat`. Alternatively, use the same Python environment as eTracker: `python reset_ajvtb_password.py`.
4. Enter your new password twice (at least 12 characters). Typing is hidden; this is normal. The password is never printed or stored as plain text.
5. Wait for Success, restart eTracker, and sign in with username `AJVTB` and the password you just chose. Username matching is case-sensitive; use the exact username printed by the tool.

The tool makes a SQLite backup in `account-reset-backups` before updating the password. Keep that backup private on your computer. It changes only the existing AJVTB user's password hash, retaining the Chief role, other accounts, and application records. It does not create a missing account or database. The separate Chief approval password is unchanged.

If your startup uses `ETRACKER_DB`, this tool reads that same variable. You can also select the active database explicitly:

```bat
python reset_ajvtb_password.py --database "C:\path\to\etracker.db"
```

If Werkzeug is missing, run the script using eTracker's existing Python/virtual environment rather than a different Python installation. Do not replace your database with another copy to reset a password.
