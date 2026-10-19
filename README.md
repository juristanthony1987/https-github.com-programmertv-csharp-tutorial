# eTracker updates

## Current update: SQLite flow, monitoring, and releasing

PostgreSQL migration is ON HOLD. This update targets the current SQLite eTracker.

[Download etracker-flow-update.zip](https://github.com/juristanthony1987/https-github.com-programmertv-csharp-tutorial/raw/refs/heads/main/etracker-flow-update.zip)

Alternatively select **Code > Download ZIP**, extract that archive, then extract the inner **etracker-flow-update.zip**. Use this new flow ZIP rather than the older UI-only or PostgreSQL packages.

Changes requested:

1. Remove Switch Workspace from the sidebar.
2. Use Acted and Total Acted Applications across application monitoring and reports.
3. Use Acted and release in the workflow guide.
4. Give `edbermelad` separate SPELS and COE monitoring dashboards for ALL RO-received records, plus an audited client release screen. Records received by other staff are included. Other receiver/verifier accounts retain their current permissions.

Stop eTracker and back up the ENTIRE existing project, including BOTH SQLite databases, before replacing included source files. Keep your existing databases, Python environment, and secret settings. Restart your normal SQLite app and refresh the browser. No PostgreSQL migration is needed.

Read [FLOW-UPDATE.md](FLOW-UPDATE.md) for installation, release rules, and validation details.

Validation: nine receiving/monitoring/releasing regression tests and four existing UI regression tests passed using temporary databases. Desktop and mobile browser checks passed, including actual release-form submission on synthetic data. Existing-record copies rendered correctly. Original database checksums stayed unchanged.

No databases, account password values, record exports, or credentials are published in these packages. They are updates, not a complete application.

## Earlier packages

- `etracker-ui-update.zip`: earlier SQLite UI update.
- `etracker-postgresql-update.zip`: saved PostgreSQL migration package, currently deferred.
