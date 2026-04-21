---
type: community
cohesion: 0.08
members: 36
---

# Data Bootstrap & DB State

**Cohesion:** 0.08 - loosely connected
**Members:** 36 nodes

## Members
- [[Contract loadAllData is the ONLY writer of DB. fields]] - code - graphify-in/kepei-app.js
- [[DB (global state object)]] - code - graphify-in/kepei-app.js
- [[DB.coa]] - code - graphify-in/kepei-app.js
- [[DB.fixed_assets]] - code - graphify-in/kepei-app.js
- [[DB.gst_ledger]] - code - graphify-in/kepei-app.js
- [[DB.inventory]] - code - graphify-in/kepei-app.js
- [[DB.invites]] - code - graphify-in/kepei-app.js
- [[DB.invoices]] - code - graphify-in/kepei-app.js
- [[DB.items]] - code - graphify-in/kepei-app.js
- [[DB.parties]] - code - graphify-in/kepei-app.js
- [[DB.projects]] - code - graphify-in/kepei-app.js
- [[DB.setup]] - code - graphify-in/kepei-app.js
- [[DB.tds]] - code - graphify-in/kepei-app.js
- [[DB.time_entries]] - code - graphify-in/kepei-app.js
- [[DB.transactions]] - code - graphify-in/kepei-app.js
- [[DEFAULT_COA constant]] - code - graphify-in/kepei-app.js
- [[Firebase Auth]] - code - graphify-in/kepei-app.js
- [[Firebase Firestore (db)]] - code - graphify-in/kepei-app.js
- [[Rationale loadAllData as narrow-waist between persistence and app state]] - code - graphify-in/kepei-app.js
- [[Rationale re-throw on load failure to fail fast instead of rendering empty state]] - code - graphify-in/kepei-app.js
- [[addRecord]] - code - graphify-in/kepei-app.js
- [[deleteRecord]] - code - graphify-in/kepei-app.js
- [[doLogin]] - code - graphify-in/kepei-app.js
- [[generateInvoiceHTML]] - code - graphify-in/kepei-app.js
- [[getGSTRegime]] - code - graphify-in/kepei-app.js
- [[loadAllData]] - code - graphify-in/kepei-app.js
- [[loadDashboard]] - code - graphify-in/kepei-app.js
- [[loadProjects]] - code - graphify-in/kepei-app.js
- [[loadTDS]] - code - graphify-in/kepei-app.js
- [[loadTransactions]] - code - graphify-in/kepei-app.js
- [[saveAllData]] - code - graphify-in/kepei-app.js
- [[saveCollection]] - code - graphify-in/kepei-app.js
- [[saveModal]] - code - graphify-in/kepei-app.js
- [[saveSetup]] - code - graphify-in/kepei-app.js
- [[updateRecord]] - code - graphify-in/kepei-app.js
- [[v1-v2-v3 Subcollection Migration]] - code - graphify-in/kepei-app.js

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Data_Bootstrap_&_DB_State
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Roles & Invite Flow]]

## Top bridge nodes
- [[loadAllData]] - degree 23, connects to 1 community
- [[saveModal]] - degree 5, connects to 1 community
- [[saveSetup]] - degree 3, connects to 1 community