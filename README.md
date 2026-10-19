# eTracker updates

## Latest: monitoring filters and separate tracker navigation

PostgreSQL migration remains ON HOLD. This update is for the existing SQLite eTracker.

[Download etracker-monitoring-update.zip](https://github.com/juristanthony1987/https-github.com-programmertv-csharp-tutorial/raw/refs/heads/main/etracker-monitoring-update.zip)

Alternatively choose **Code > Download ZIP**, extract that archive, then extract the inner **etracker-monitoring-update.zip**.

### Current changes

- Processing Status and Office filters work together with the report period and search. Apply Filters replaces Update monitoring. Filtered counts and records stay consistent, and filters remain active across cards and pagination. Releasing shows the same status/office filters alongside its search.
- SPELS and COE use the Go to dropdown as the system switch. Cross-system monitoring/releasing tabs are removed, and the sidebar follows the selected tracker. Each dashboard, queue, release view, and record list uses only that system's records.

- Releasing opens its own focused view with Ready for Release, Released to Client, and a dedicated search bar for reference numbers, applicant names, or offices. Search is preserved across release queues and pages.
- SPELS Monitoring alerts edbermelad about pending applications at 15–20 working days (amber) and beyond 20 working days (red). Active COPI pauses are excluded; recorded hold days are deducted after resuming. The alert opens the affected records and uses current pending records across receipt years.

- Received Applications replaces New Applications.
- SPELS Monitoring shows carried pending, received, pending, acted within/beyond 20 working days, and Total Acted Applications. Pending includes unresolved awaiting/in-progress applications and has a red indicator.
- Admin and SPELS Monitoring share report-period and working-day calculations, including recorded holidays, COPI holds, Chief adjustments, and HGE quantities.
- Receiving queue is blue and Releasing is teal. The sidebar follows the selected tracker; system switching uses Go to. COE retains its existing status-based monitoring.
- Admin transaction and dashboard record tables show Received by, Processing Status, Verification Stage, and Client Release.
- Pagination has numbered pages, Previous/Next controls, an active-page highlight, record ranges, and preserved filters.
- Earlier receiving/releasing permissions and audit history remain included.

Stop eTracker and back up the ENTIRE existing project, including BOTH databases, before replacing included files. Extract the inner update ZIP into the existing project beside app.py, replace ALL included files together, keep your databases and secret settings, restart using the normal SQLite command, then refresh with Ctrl+F5.

See [FLOW-UPDATE.md](FLOW-UPDATE.md) for exact report scope, release behavior, installation, and validation details.

Validation: sixteen monitoring/releasing/reporting regression tests and four existing UI tests passed using temporary databases. Browser checks covered combined status/office filtering, matching summary totals, pagination, mobile layouts, release filters, clearing filters, and switching through Go to without mixing systems. Earlier checks also covered actual release submission and pending alerts. Existing-record copies rendered correctly; original database checksums remained unchanged. Actual office-PC installation is still performed by the user.

Packages contain source and instructions only, not databases, account password values, or record exports.

## Earlier packages

- etracker-flow-update.zip: previous SQLite flow update.
- etracker-ui-update.zip: earlier UI update.
- etracker-postgresql-update.zip: saved PostgreSQL package, currently deferred.

## AJVTB account recovery

[Download etracker-ajvtb-reset.zip](https://github.com/juristanthony1987/https-github.com-programmertv-csharp-tutorial/raw/refs/heads/main/etracker-ajvtb-reset.zip)

Stop eTracker, copy the two reset tools beside app.py and the active etracker.db, then run RESET-AJVTB.bat. Choose your own new password using the hidden prompts. A local database backup is created before updating only the existing AJVTB sign-in password. See [account-recovery/README.md](account-recovery/README.md). The separate Chief approval password is unchanged.

Recovery validation: five temporary-database tests passed, and the actual Flask login accepted the new password while rejecting the old one. No office-PC password has been changed by the cloud environment. The download contains tools and instructions, without any database or password.
