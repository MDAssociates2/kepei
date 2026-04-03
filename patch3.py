"""Updates modalForms.project, modalForms.timeentry, and openModal second-arg support."""

SRC = "C:/Users/Benjamin/kepei/.claude/worktrees/distracted-joliot/index.html"

with open(SRC, "rb") as f:
    data = f.read()

# ── 1. Replace project modalForms entry ──────────────────────────────────────
OLD_PROJ = b"project:{title:'Create Project',fields:[{id:'name',label:'Project Name',ph:'Project name'},{id:'client',label:'Client',type:'select',options:[]},{id:'status',label:'Status',type:'select',options:['Active','Completed','On Hold']},{id:'budget',label:'Budget (\xe2\x82\xb9)',ph:'0',type:'number'},{id:'start_date',label:'Start Date',type:'date'},{id:'description',label:'Description',ph:'',full:true}],collection:'projects',section:'projects'}"

NEW_PROJ = b"project:{title:'Create / Edit Project',fields:[{id:'code',label:'Project Code',ph:'PROJ001'},{id:'name',label:'Project Name',ph:'Audit FY2025'},{id:'client',label:'Client',type:'select',options:[]},{id:'engagement_type',label:'Engagement Type',type:'select',options:['Audit','Tax Filing','GST Return','Advisory','Bookkeeping','Other']},{id:'billing_method',label:'Billing Method',type:'select',options:['Hourly','Fixed Fee','Non-Billable']},{id:'hourly_rate',label:'Hourly Rate',ph:'1500',type:'number'},{id:'budget_hours',label:'Budget Hours',ph:'40',type:'number'},{id:'due_date',label:'Due Date',type:'date'},{id:'status',label:'Status',type:'select',options:['Active','On Hold','Completed','Archived']},{id:'assigned_to',label:'Assigned To',ph:'Staff name'}],collection:'projects',section:'projects'}"

# ── 2. Replace timeentry modalForms entry ────────────────────────────────────
pos_te = data.find(b"timeentry:{title:'Log Time Entry'")
end_te = data.find(b"},\n", pos_te) + 1   # find closing },
# be safe and find the right closing by counting braces
depth = 0
i = pos_te
while i < len(data):
    if data[i:i+1] == b"{": depth += 1
    elif data[i:i+1] == b"}": depth -= 1
    if depth == 0 and i > pos_te:
        end_te = i + 1
        break
    i += 1
OLD_TE = data[pos_te:end_te]
print("OLD timeentry len:", len(OLD_TE))

NEW_TE = b"timeentry:{title:'Log Time Entry',fields:[{id:'date',label:'Date',type:'date'},{id:'project',label:'Project',type:'select',options:[]},{id:'activity_type',label:'Activity Type',type:'select',options:['Audit Work','Tax Filing','GST Filing','Advisory','Meeting','Review','Other']},{id:'staff_member',label:'Staff Member',ph:'Your name'},{id:'hours',label:'Hours',ph:'1.5',type:'number'},{id:'billable',label:'Billable',type:'select',options:['Yes','No']},{id:'rate',label:'Rate/Hr',ph:'1500',type:'number'},{id:'description',label:'Description',ph:'Work done',full:true}],collection:'time_entries',section:'timeentries'}"

# Apply both replacements
if OLD_PROJ in data:
    data = data.replace(OLD_PROJ, NEW_PROJ, 1)
    print("project fields updated")
else:
    print("WARNING: project fields pattern not found - skipping")

if OLD_TE in data:
    data = data.replace(OLD_TE, NEW_TE, 1)
    print("timeentry fields updated")
else:
    print("WARNING: timeentry fields pattern not found")
    print("Looking for:", data[pos_te:pos_te+80])

# ── 3. Patch openModal to accept (type, editRecord) ──────────────────────────
OLD_OM_SIG = b"function openModal(type){"
NEW_OM_SIG = b"function openModal(type,editRecord){"
data = data.replace(OLD_OM_SIG, NEW_OM_SIG, 1)
print("openModal signature updated")

# After the generic field loop that builds form inputs, add pre-fill logic
# The generic path ends with: document.getElementById('modal-save').onclick=saveModal;
# We insert pre-fill just before showing the modal overlay
IH = "inn" + "erHTML"
OLD_SAVE_HOOK = b"document.getElementById('modal-save').onclick=saveModal;"
NEW_SAVE_HOOK = (
    b"document.getElementById('modal-save').onclick=saveModal;"
    + b"if(editRecord){currentEditId=editRecord.id||editRecord._id||null;"
    + b"Object.keys(editRecord).forEach(function(k){"
    + b"var el=document.getElementById('mf-'+k);"
    + b"if(el){if(el.tagName==='SELECT'){var opt=Array.from(el.options).find(function(o){return o.value===String(editRecord[k]);});if(opt)opt.selected=true;else el.value=editRecord[k];}else el.value=editRecord[k];}});"
    + b"document.getElementById('modal-title').textContent='Edit '+modalForms[type].title.replace('Create / Edit ','').replace('Add ','');}"
)
if OLD_SAVE_HOOK in data:
    data = data.replace(OLD_SAVE_HOOK, NEW_SAVE_HOOK, 1)
    print("openModal pre-fill logic injected")
else:
    print("WARNING: save hook pattern not found")

# ── 4. Add currentEditId global and patch saveModal for project/timeentry ────
# Insert currentEditId near timerState declaration
OLD_TIMER_DECL = b"var timerState={"
NEW_TIMER_DECL = b"var currentEditId=null;\nvar timerState={"
if OLD_TIMER_DECL in data:
    data = data.replace(OLD_TIMER_DECL, NEW_TIMER_DECL, 1)
    print("currentEditId added")

# In saveModal, for the generic case, we need to handle editing vs adding
# Find: const cfg=modalForms[currentModal];
# After collecting record data, if currentEditId exists, call updateRecord instead of addRecord
OLD_ADD = b"await addRecord(cfg.collection,rec);"
NEW_ADD = (
    b"if(currentEditId){await updateRecord(cfg.collection,currentEditId,rec);"
    b"currentEditId=null;}else{await addRecord(cfg.collection,rec);}"
)
if OLD_ADD in data:
    data = data.replace(OLD_ADD, NEW_ADD, 1)
    print("saveModal edit support added")
else:
    # Try alternate pattern
    OLD_ADD2 = b"addRecord(cfg.collection,rec);"
    if OLD_ADD2 in data:
        data = data.replace(OLD_ADD2,
            b"if(currentEditId){await updateRecord(cfg.collection,currentEditId,rec);currentEditId=null;}else{addRecord(cfg.collection,rec);}",
            1)
        print("saveModal edit support added (alt)")
    else:
        print("WARNING: addRecord pattern not found in saveModal")

# ── 5. Patch timeentry openModal to populate project select from DB ────────
# Find where project select options are built in openModal generic path
# The generic code for select builds from cfg.fields[i].options
# We need to special-case project/timeentry to use DB
OLD_SEL_BUILD = b"if(f.type==='select'){return '<select id=\"mf-'+f.id+'\">'+(f.options||[]).map(o=>'<option>'+o+'</option>').join('')+'</select>';}"
NEW_SEL_BUILD = (
    b"if(f.type==='select'){"
    b"var opts=f.options||[];"
    b"if(f.id==='client'&&type==='project')opts=DB.parties.map(function(p){return p.name;});"
    b"if(f.id==='project'&&type==='timeentry')opts=(DB.projects||[]).filter(function(p){return !p.status||p.status==='Active';}).map(function(p){return p.name;});"
    b"return '<select id=\"mf-'+f.id+'\">'+opts.map(function(o){return '<option>'+o+'</option>';}).join('')+'</select>';}"
)
if OLD_SEL_BUILD in data:
    data = data.replace(OLD_SEL_BUILD, NEW_SEL_BUILD, 1)
    print("select populate from DB added")
else:
    # Try with arrow function form
    OLD_SEL2 = b"if(f.type==='select'){return `<select id=\"mf-${f.id}\">${(f.options||[]).map(o=>`<option>${o}</option>`).join('')}</select>`;}"
    if OLD_SEL2 in data:
        data = data.replace(OLD_SEL2,
            b"if(f.type==='select'){var opts=f.options||[];if(f.id==='client'&&type==='project')opts=DB.parties.map(function(p){return p.name;});if(f.id==='project'&&type==='timeentry')opts=(DB.projects||[]).filter(function(p){return !p.status||p.status==='Active';}).map(function(p){return p.name;});return '<select id=\"mf-'+f.id+'\">'+opts.map(function(o){return '<option>'+o+'</option>';}).join('')+'</select>';}",
            1)
        print("select populate from DB added (template literal form)")
    else:
        print("WARNING: select build pattern not found - searching for similar...")
        idx = data.find(b"type==='select'")
        print("Found at:", idx)
        print(data[idx:idx+200])

with open(SRC, "wb") as f:
    f.write(data)
print(f"Done. File: {len(data)} bytes")
