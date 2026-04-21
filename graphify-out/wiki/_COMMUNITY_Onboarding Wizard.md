---
type: community
cohesion: 0.33
members: 7
---

# Onboarding Wizard

**Cohesion:** 0.33 - loosely connected
**Members:** 7 nodes

## Members
- [[genRecs()]] - code - graphify-in\kepei-app.js
- [[initWizard()]] - code - graphify-in\kepei-app.js
- [[showOnboarding()]] - code - graphify-in\kepei-app.js
- [[showWizStep()]] - code - graphify-in\kepei-app.js
- [[updateStepDots()]] - code - graphify-in\kepei-app.js
- [[wizBack()]] - code - graphify-in\kepei-app.js
- [[wizNext()]] - code - graphify-in\kepei-app.js

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Onboarding_Wizard
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_App Init & Auth]]
- 1 edge to [[_COMMUNITY_Roles & Invite Flow]]

## Top bridge nodes
- [[wizNext()]] - degree 4, connects to 2 communities
- [[showWizStep()]] - degree 5, connects to 1 community
- [[initWizard()]] - degree 3, connects to 1 community
- [[showOnboarding()]] - degree 3, connects to 1 community
- [[updateStepDots()]] - degree 3, connects to 1 community