# eTracker flow update — 19 October 2026

For the current SQLite eTracker installation. PostgreSQL migration remains on hold. This is an update package, not the complete application.

## Changes requested

1. Removed the Switch Workspace sidebar link. The existing system selector and SPELS/COE dropdown remain available.
2. Changed application-report wording to Acted and Total Acted Applications across dashboard cards, report headers, CSV headings, and IPMR application-total labels. Working-day computations and the Approved/Disapproved report rule are retained.
3. Updated workflow step 4 to Acted and release and adjusted related help text.
4. Added separate SPELS Monitoring and COE Monitoring dashboards to the enabled receiver account `edbermelad`. They include all applications received at RO, including those received by other accounts. Field Office applications that have not reached RO stay in the receiving queue.

## Install

1. Stop eTracker with Ctrl+C in its terminal.
2. Back up the ENTIRE existing project, including both `etracker.db` and `coe.db`.
3. Extract `etracker-flow-update.zip` into the existing project folder beside `app.py`. Replace ALL included source and template files together.
4. Keep both existing databases, your virtual environment, and existing secret settings.
5. Restart with your current SQLite startup command and refresh the browser with Ctrl+F5. Sign out and back in as `edbermelad`.

This package contains no databases, password values, account exports, or new third-party dependencies. Do not install it over a PostgreSQL deployment; it targets the current SQLite version.

## Receiving and releasing

The designated account keeps the Receiving Queue and gains SPELS Monitoring and COE Monitoring. Dashboards show total received applications, Total Acted Applications, ready-for-release applications, releases to clients, in-progress applications, and holds. HGE quantities count applications; table counts refer to records. Status counts represent different aspects of processing and can overlap.

Use the Releasing button or Ready for Release card. Open an application, enter the actual client release date, then select Confirm client release. Applications still waiting for checks show View status instead.

The account can monitor all RO records but cannot change applicant details, verification fields, office assignments, or select an arbitrary processing action through the release form. Other receiver/verifier accounts retain their existing permissions. No existing passwords or account roles are changed.

SPELS release uses an already saved Approved/Disapproved action, or retains an existing Released action. If both verification stages have completed and the Second Verifier's saved action is Approved/Disapproved, recording release carries that saved action into the normal reporting fields. It does not invent a new decision. First and Second Processor names/dates are required. Pending records remain blocked; outstanding FO handoffs require receipt confirmation.

COE release requires a saved ready/released status or completed second verification with a saved Approved/Disapproved action. Compliance/COPI holds and incomplete handoffs block release. Saving records the actual client date and Released status.

Receipt and verification dates are retained. Each release writes an audit entry under `edbermelad`. The form rejects future dates, dates preceding recorded receipt/processing/handoffs, stale forms, unexpected fields, and invalid CSRF tokens. An already recorded release date is read-only here; corrections continue through existing administrator workflows.

## Validation

Run separately from the project directory:

```bat
python -m unittest test_ui_flow -v
python -m unittest test_receiver_monitoring -v
```

Four existing UI regressions and nine receiving/monitoring/releasing regressions passed using temporary databases. Desktop and mobile browser checks passed, including a real form release on synthetic data. The new dashboards and queues also rendered with development copies of existing records. Original database checksums remained unchanged. Actual office-PC installation has not been performed by the cloud environment.
