---
type: community
cohesion: 0.29
members: 7
---

# OCR Processing

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[displayOCRResult()]] - code - graphify-in\kepei-app.js
- [[extractOCRFields()]] - code - graphify-in\kepei-app.js
- [[handleOCRDrop()]] - code - graphify-in\kepei-app.js
- [[handleOCRFile()]] - code - graphify-in\kepei-app.js
- [[processOCRText()]] - code - graphify-in\kepei-app.js
- [[runTesseractOCR()]] - code - graphify-in\kepei-app.js
- [[setOCRProgress()]] - code - graphify-in\kepei-app.js

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OCR_Processing
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_App Init & Auth]]
- 3 edges to [[_COMMUNITY_Ageing Analysis & Client Forms]]
- 1 edge to [[_COMMUNITY_Roles & Invite Flow]]

## Top bridge nodes
- [[handleOCRFile()]] - degree 5, connects to 3 communities
- [[runTesseractOCR()]] - degree 5, connects to 2 communities
- [[displayOCRResult()]] - degree 3, connects to 2 communities
- [[processOCRText()]] - degree 4, connects to 1 community
- [[extractOCRFields()]] - degree 2, connects to 1 community