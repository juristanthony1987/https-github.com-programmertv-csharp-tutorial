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
3. Extract the latest `etracker-monitoring-update.zip` into the existing project folder beside `app.py`. Replace ALL included source and template files together.
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


## Monitoring and admin refinements — latest update

- The admin receipt card now reads Received Applications, not New Applications.
- SPELS Monitoring now shows Carried Pending, Received Applications, Pending Applications, Acted within 20 working days, Acted beyond 20 working days, and Total Acted Applications. Pending totals include unresolved Received and On Process applications, not only explicit Pending/COPI/Compliance statuses. Nonzero pending counts have a red card, badge, and highlighted record rows.
- Admin reports and SPELS Monitoring share the same receipt/action-period classification and working-day calculator. Working days are inclusive, exclude recorded holidays and COPI holds, and retain Chief adjustments. Exactly 20 working days is within; 21 is beyond. HGE batches use their quantities.
- Report filters use application Date Received for receipts, action date for acted activity, and the period cutoff for unresolved applications. Thus an older receipt acted on during the selected month is included. The report defaults to the current year. Choosing a month with All years uses the current year. All years without a month is cumulative.
- Monitoring is limited to applications recorded as received at RO. Historical aggregate balances without individual RO-receipt records remain visible in the admin report, with a notice in monitoring. This is a scope difference, not a second working-day formula.
- Ready for Release and Released to Client remain separate LIVE queues across receipt years, using the search filter. They do not replace performance counts or lose older applications when a report month is selected.
- COE remains available from the Go to dropdown; the duplicate COE Monitoring sidebar link is removed. COE retains its existing status-based monitoring and release workflow. This update does not introduce a new COE 20-day counting policy.
- Receiving queue is blue; Releasing is teal.
- Admin Transactions and dashboard record lists include Received by, Processing Status, Verification Stage, and Client Release. Verification progress is displayed separately from the processing action.
- Record pagination now has Previous/Next, numbered pages, an active page, disabled boundary controls, and displayed record ranges. Search and report filters are preserved on page changes.

Validation now includes 12 monitoring/releasing/reporting regressions plus four existing UI regressions. Browser checks covered both receiver and admin Next/Previous navigation, filter retention, mobile layouts, pending highlights, and the two action-button colors. Existing-record copies rendered successfully; original database files were unchanged.


## Focused releasing and pending-action alerts — latest addition

- Selecting Releasing or either release summary card opens a focused release view for SPELS or COE. It shows only the release summaries and the selected release list, with a dedicated Search applications bar. The performance cards, report-period controls, and pending alerts are omitted from this view.
- Search accepts reference numbers, applicant names, or offices. Search remains active when switching between Ready for Release and Released to Client or changing pages. Clear search resets the query while retaining the selected release queue. Releasing includes all RO receipt years, independently of monitoring-period filters.
- The release detail page returns to Releasing. After confirming a release, the Released to Client queue opens.
- SPELS Monitoring for edbermelad now shows a current pending-action alert when an unresolved, unpaused application reaches 15 counted working days. Amber indicates 15–20 working days; the bar turns red if any matching application exceeds 20 working days. View applications opens the matching records, oldest counted age first. HGE quantities count applications.
- Alerts use current pending records across all RO receipt years, independently of the selected report period. The monitoring search still applies. Active recorded COPI pauses are excluded. Resumed records become eligible again based on working days after deducting recorded COPI hold days, weekends, and holidays. No new COE deadline policy is introduced.

Validation: 14 monitoring/releasing/reporting tests and four existing UI tests passed on temporary databases. Browser checks covered the alert link, release-only view, search, filtered pagination, mobile layout, an actual release form submission, and COE releasing. Original database checksums remained unchanged.

The extra Search this list forms above monitoring tables have been removed at the user's request. Use the main monitoring search or the dedicated Releasing search.
