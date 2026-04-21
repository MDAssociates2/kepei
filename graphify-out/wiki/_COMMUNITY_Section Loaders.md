---
type: community
cohesion: 0.22
members: 9
---

# Section Loaders

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[filterGST()]] - code - graphify-in\kepei-app.js
- [[loadGSTLedger()]] - code - graphify-in\kepei-app.js
- [[loadInventory()]] - code - graphify-in\kepei-app.js
- [[loadInvoices()]] - code - graphify-in\kepei-app.js
- [[loadItems()]] - code - graphify-in\kepei-app.js
- [[loadParties()]] - code - graphify-in\kepei-app.js
- [[loadTransactions()]] - code - graphify-in\kepei-app.js
- [[toggleClientView()]] - code - graphify-in\kepei-app.js
- [[updateBadges()]] - code - graphify-in\kepei-app.js

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Section_Loaders
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_App Init & Auth]]
- 2 edges to [[_COMMUNITY_Ageing Analysis & Client Forms]]
- 1 edge to [[_COMMUNITY_Roles & Invite Flow]]

## Top bridge nodes
- [[loadTransactions()]] - degree 5, connects to 3 communities
- [[updateBadges()]] - degree 8, connects to 2 communities
- [[loadGSTLedger()]] - degree 3, connects to 1 community
- [[filterGST()]] - degree 2, connects to 1 community
- [[loadInventory()]] - degree 2, connects to 1 community