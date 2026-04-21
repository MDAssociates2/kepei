---
type: community
cohesion: 0.16
members: 18
---

# OCR Processing

**Cohesion:** 0.16 - loosely connected
**Members:** 18 nodes

## Members
- [[closeClientForm()]] - code - graphify-in\kepei-app.js
- [[displayOCRResult()]] - code - graphify-in\kepei-app.js
- [[drillPartyAgeing()]] - code - graphify-in\kepei-app.js
- [[esc()]] - code - graphify-in\kepei-app.js
- [[extractOCRFields()]] - code - graphify-in\kepei-app.js
- [[fmt()]] - code - graphify-in\kepei-app.js
- [[handleOCRDrop()]] - code - graphify-in\kepei-app.js
- [[handleOCRFile()]] - code - graphify-in\kepei-app.js
- [[loadClientRecentTxns()]] - code - graphify-in\kepei-app.js
- [[loadITCSummary()]] - code - graphify-in\kepei-app.js
- [[loadStockSummary()]] - code - graphify-in\kepei-app.js
- [[markITCClaimed()]] - code - graphify-in\kepei-app.js
- [[processOCRText()]] - code - graphify-in\kepei-app.js
- [[runTesseractOCR()]] - code - graphify-in\kepei-app.js
- [[saveClientEntry()]] - code - graphify-in\kepei-app.js
- [[setOCRProgress()]] - code - graphify-in\kepei-app.js
- [[showClientJournal()]] - code - graphify-in\kepei-app.js
- [[updateRecord()]] - code - graphify-in\kepei-app.js

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OCR_Processing
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_Auth & Roles]]
- 6 edges to [[_COMMUNITY_Auth & Roles]]
- 2 edges to [[_COMMUNITY_Section Loaders]]
- 2 edges to [[_COMMUNITY_Section Loaders]]
- 1 edge to [[_COMMUNITY_Modal Dispatcher & Writes]]

## Top bridge nodes
- [[fmt()]] - degree 11, connects to 3 communities
- [[showClientJournal()]] - degree 7, connects to 3 communities
- [[saveClientEntry()]] - degree 8, connects to 2 communities
- [[handleOCRFile()]] - degree 5, connects to 2 communities
- [[markITCClaimed()]] - degree 4, connects to 2 communities