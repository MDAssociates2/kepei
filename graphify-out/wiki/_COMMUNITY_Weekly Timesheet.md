---
type: community
cohesion: 0.50
members: 4
---

# Weekly Timesheet

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[loadBulkEntry()]] - code - graphify-in\kepei-app.js
- [[loadWeeklyTimesheet()]] - code - graphify-in\kepei-app.js
- [[shiftWeek()]] - code - graphify-in\kepei-app.js
- [[switchTimeTab()]] - code - graphify-in\kepei-app.js

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Weekly_Timesheet
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_App Init & Auth]]

## Top bridge nodes
- [[loadWeeklyTimesheet()]] - degree 3, connects to 1 community
- [[switchTimeTab()]] - degree 3, connects to 1 community
- [[loadBulkEntry()]] - degree 2, connects to 1 community
- [[shiftWeek()]] - degree 2, connects to 1 community