# eTracker updates

## Latest: PostgreSQL for an office PC

[Download the PostgreSQL update ZIP](https://github.com/juristanthony1987/https-github.com-programmertv-csharp-tutorial/raw/refs/heads/main/etracker-postgresql-update.zip)

Alternatively select **Code > Download ZIP**, extract it, then open the inner **etracker-postgresql-update.zip**.

This is an update for the existing project supplied as `etracker2026(New).zip`, not a complete application. It includes the shared UI update plus PostgreSQL support, a read-only SQLite-to-PostgreSQL migration, Windows launcher, and regression tests.

1. Stop the application and back up the entire current project, including BOTH SQLite databases.
2. Extract the inner update ZIP into the existing project folder.
3. Read **START-HERE-POSTGRESQL.txt** and **POSTGRESQL-SETUP.md** before proceeding.
4. Install PostgreSQL on the central office PC and create the dedicated app role/database.
5. Install requirements, migrate, check, then start using the PostgreSQL launcher.

The update does not migrate your PC automatically. Existing accounts are retained during migration. No databases, record exports, backups, or credentials are included here.

Validation: nine real-PostgreSQL integration tests and four SQLite regression tests passed. Tested ten concurrent SPELS saves and ten concurrent COE saves, unique references, office scope/guards, stale-edit rejection, review resolution, COPI/date triggers, rollback, and refusal of nonempty migration targets. Existing SQLite data was verified across all imported fields in the test environment; PostgreSQL backup/restore was also checked. Validate the actual office deployment before staff use it.

## Previous SQLite UI update

`etracker-ui-update.zip` is the earlier UI-only update. Its instructions are in `UI-UPDATE.md` inside that ZIP. For the latest PostgreSQL update, use the file named **etracker-postgresql-update.zip** above.
