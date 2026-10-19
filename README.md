# eTracker updates

## Latest: focused releasing, search, and pending alerts

PostgreSQL migration remains ON HOLD. This update is for the existing SQLite eTracker.

[Download etracker-monitoring-update.zip](https://github.com/juristanthony1987/https-github.com-programmertv-csharp-tutorial/raw/refs/heads/main/etracker-monitoring-update.zip)

Alternatively choose **Code > Download ZIP**, extract that archive, then extract the inner **etracker-monitoring-update.zip**.

### Current changes

- Releasing opens its own focused view with Ready for Release, Released to Client, and a dedicated search bar for reference numbers, applicant names, or offices. Search is preserved across release queues and pages.
- SPELS Monitoring alerts edbermelad about pending applications at 15–20 working days (amber) and beyond 20 working days (red). Active COPI pauses are excluded; recorded hold days are deducted after resuming. The alert opens the affected records and uses current pending records across receipt years.

- Received Applications replaces New Applications.
- SPELS Monitoring shows carried pending, received, pending, acted within/beyond 20 working days, and Total Acted Applications. Pending includes unresolved awaiting/in-progress applications and has a red indicator.
- Admin and SPELS Monitoring share report-period and working-day calculations, including recorded holidays, COPI holds, Chief adjustments, and HGE quantities.
- Receiving queue is blue and Releasing is teal. The redundant COE Monitoring sidebar link is removed; COE remains in Go to. COE retains its existing status-based monitoring.
- Admin transaction and dashboard record tables show Received by, Processing Status, Verification Stage, and Client Release.
- Pagination has numbered pages, Previous/Next controls, an active-page highlight, record ranges, and preserved filters.
- Earlier receiving/releasing permissions and audit history remain included.

Stop eTracker and back up the ENTIRE existing project, including BOTH databases, before replacing included files. Extract the inner update ZIP into the existing project beside app.py, replace ALL included files together, keep your databases and secret settings, restart using the normal SQLite command, then refresh with Ctrl+F5.

See [FLOW-UPDATE.md](FLOW-UPDATE.md) for exact report scope, release behavior, installation, and validation details.

Validation: fourteen monitoring/releasing/reporting regression tests and four existing UI tests passed using temporary databases. Browser checks covered release-only navigation, search, filter retention, mobile layouts, actual release submission, and the pending-alert queue, in addition to earlier admin pagination checks. Existing-record copies rendered correctly; original database checksums remained unchanged. Actual office-PC installation is still performed by the user.

Packages contain source and instructions only, not databases, account password values, or record exports.

## Earlier packages

- etracker-flow-update.zip: previous SQLite flow update.
- etracker-ui-update.zip: earlier UI update.
- etracker-postgresql-update.zip: saved PostgreSQL package, currently deferred.
