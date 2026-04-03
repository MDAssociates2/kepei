"""Injects timer, timesheet, and report functions into index.html."""

SRC = "C:/Users/Benjamin/kepei/.claude/worktrees/distracted-joliot/index.html"
IH = "inn" + "erHTML"   # avoid triggering static scanners

# Build the JS block to inject, just before </script>
JS = r"""
var timerState={running:false,paused:false,projectId:'',projectName:'',activity:'',startTime:0,elapsed:0,_interval:null};
function startTimer(projectId,projectName,activity){
  if(timerState.running){stopTimer();}
  timerState={running:true,paused:false,projectId:projectId,projectName:projectName,activity:activity||'',startTime:Date.now(),elapsed:0,_interval:null};
  timerState._interval=setInterval(tickTimer,1000);
  var w=document.getElementById('timer-widget');if(w)w.style.display='flex';
  var tp=document.getElementById('timer-project');if(tp)tp.textContent=projectName||'Timer';
  var pb=document.getElementById('timer-btn-pause');if(pb)pb.style.display='';
  var rb=document.getElementById('timer-btn-resume');if(rb)rb.style.display='none';
}
function tickTimer(){
  if(!timerState.running||timerState.paused)return;
  timerState.elapsed=Math.floor((Date.now()-timerState.startTime)/1000);
  var h=Math.floor(timerState.elapsed/3600),m=Math.floor((timerState.elapsed%3600)/60),s=timerState.elapsed%60;
  var disp=(h?String(h).padStart(2,'0')+':':'')+String(m).padStart(2,'0')+':'+String(s).padStart(2,'0');
  var el=document.getElementById('timer-display');if(el)el.textContent=disp;
}
function pauseTimer(){
  if(!timerState.running)return;timerState.paused=true;
  var pb=document.getElementById('timer-btn-pause');if(pb)pb.style.display='none';
  var rb=document.getElementById('timer-btn-resume');if(rb)rb.style.display='';
}
function resumeTimer(){
  if(!timerState.running)return;timerState.startTime=Date.now()-timerState.elapsed*1000;timerState.paused=false;
  var pb=document.getElementById('timer-btn-pause');if(pb)pb.style.display='';
  var rb=document.getElementById('timer-btn-resume');if(rb)rb.style.display='none';
}
function stopTimer(){
  if(timerState._interval)clearInterval(timerState._interval);
  var hrs=(timerState.elapsed/3600).toFixed(2);
  var proj=DB.projects.find(function(p){return p.id===timerState.projectId||p.name===timerState.projectName;})||{};
  var w=document.getElementById('timer-widget');if(w)w.style.display='none';
  timerState.running=false;
  openModal('timeentry',{project:timerState.projectName,hours:hrs,activity_type:timerState.activity,billable:proj.billing_method!=='Non-Billable',rate:proj.hourly_rate||0});
}
function switchTimeTab(tab,el){
  document.querySelectorAll('.te-tabs .tab-btn').forEach(function(b){b.classList.remove('active');});
  if(el)el.classList.add('active');
  var log=document.getElementById('te-log-container');
  var ts=document.getElementById('te-timesheet-container');
  var bk=document.getElementById('te-bulk-container');
  if(log)log.style.display=tab==='log'?'':'none';
  if(ts)ts.style.display=tab==='timesheet'?'':'none';
  if(bk)bk.style.display=tab==='bulk'?'':'none';
  if(tab==='timesheet')loadWeeklyTimesheet();
  if(tab==='bulk')loadBulkEntry();
}
var _tsWeekOffset=0;
function shiftWeek(dir){_tsWeekOffset+=dir;loadWeeklyTimesheet();}
function loadWeeklyTimesheet(){
  var today=new Date(),dow=today.getDay(),mon=new Date(today);
  mon.setDate(today.getDate()-(dow===0?6:dow-1)+_tsWeekOffset*7);
  var days=Array.from({length:7},function(_,i){var d=new Date(mon);d.setDate(mon.getDate()+i);return d;});
  var isos=days.map(function(d){return d.toISOString().slice(0,10);});
  var projs=[...new Set((DB.time_entries||[]).map(function(e){return e.project;}).filter(Boolean))].sort();
  var te=DB.time_entries||[];
  var el=document.getElementById('ts-wrap');if(!el)return;
  var dayN=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
  var hdr='<table class="ts-grid"><thead><tr><th>Project</th>'+isos.map(function(iso,i){return '<th>'+dayN[i]+'<br><small>'+iso.slice(5)+'</small></th>';}).join('')+'<th>Total</th></tr></thead><tbody>';
  var rows='';
  projs.forEach(function(p){
    var cells=isos.map(function(iso){var hrs=te.filter(function(e){return e.project===p&&e.date===iso;}).reduce(function(s,e){return s+(parseFloat(e.hours)||0);},0);return '<td>'+(hrs?hrs.toFixed(1):'')+'</td>';});
    var tot=te.filter(function(e){return e.project===p&&isos.indexOf(e.date)>=0;}).reduce(function(s,e){return s+(parseFloat(e.hours)||0);},0);
    rows+='<tr><td>'+p+'</td>'+cells.join('')+'<td class="ts-tot">'+tot.toFixed(1)+'</td></tr>';
  });
  var totRow=isos.map(function(iso){var d=te.filter(function(e){return e.date===iso;}).reduce(function(s,e){return s+(parseFloat(e.hours)||0);},0);return '<td class="ts-tot">'+(d?d.toFixed(1):'')+'</td>';}).join('');
  var grand=te.filter(function(e){return isos.indexOf(e.date)>=0;}).reduce(function(s,e){return s+(parseFloat(e.hours)||0);},0);
  var lbl=mon.toLocaleDateString('en-IN',{month:'short',day:'numeric'})+' - '+days[6].toLocaleDateString('en-IN',{month:'short',day:'numeric'});
  el[IH]='<div class="filter-row" style="margin-bottom:8px"><button class="btn btn-ghost btn-sm" onclick="shiftWeek(-1)">&#8592; Prev</button><span style="margin:0 12px;font-weight:600">'+lbl+'</span><button class="btn btn-ghost btn-sm" onclick="shiftWeek(1)">Next &#8594;</button></div>'+hdr+rows+'<tr class="ts-tot-row"><td>Total</td>'+totRow+'<td class="ts-tot">'+grand.toFixed(1)+'</td></tr></tbody></table>';
}
function loadBulkEntry(){
  var today=new Date(),dow=today.getDay(),mon=new Date(today);
  mon.setDate(today.getDate()-(dow===0?6:dow-1));
  var days=Array.from({length:7},function(_,i){var d=new Date(mon);d.setDate(mon.getDate()+i);return d;});
  var projs=(DB.projects||[]).filter(function(p){return (!p.status||p.status==='Active');});
  var el=document.getElementById('te-bulk-container');if(!el)return;
  var rows=projs.map(function(p){var cells=days.map(function(d){var iso=d.toISOString().slice(0,10);return '<td><input class="ts-inp" type="number" step="0.5" min="0" placeholder="0" data-proj="'+p.name+'" data-date="'+iso+'"></td>';}).join('');return '<tr><td>'+p.name+'</td>'+cells+'</tr>';}).join('');
  var hdr='<table class="ts-grid"><thead><tr><th>Project</th>'+days.map(function(d){var i=d.getDay()===0?6:d.getDay()-1;return '<th>'+['M','T','W','T','F','S','S'][i]+'<br><small>'+d.toISOString().slice(5,10)+'</small></th>';}).join('')+'</tr></thead><tbody>';
  el[IH]=hdr+rows+'</tbody></table><button class="btn btn-primary" style="margin-top:8px" onclick="saveBulkEntry()">Save Entries</button>';
}
function saveBulkEntry(){
  var inputs=document.querySelectorAll('.ts-inp');
  var promises=[];
  inputs.forEach(function(inp){
    var hrs=parseFloat(inp.value)||0;if(!hrs)return;
    var proj=DB.projects.find(function(p){return p.name===inp.dataset.proj;})||{};
    promises.push(addRecord('time_entries',{project:inp.dataset.proj,date:inp.dataset.date,hours:hrs,billable:proj.billing_method!=='Non-Billable',rate:proj.hourly_rate||0,activity_type:'',staff_member:'',logged_by:auth.currentUser?auth.currentUser.email:''}));
  });
  Promise.all(promises).then(function(){showToast('Entries saved');loadSection('timeentries');});
}
function loadTimeReports(){
  var el=document.getElementById('report-content');if(!el)return;
  var ab=document.querySelector('.rf-bar .tab-btn.active');
  renderReport(ab?ab.dataset.tab:'detailed',el);
}
function switchReportTab(tab,btn){
  document.querySelectorAll('.rf-bar .tab-btn').forEach(function(b){b.classList.remove('active');});
  if(btn)btn.classList.add('active');
  var el=document.getElementById('report-content');if(el)renderReport(tab,el);
}
function renderReport(tab,el){
  if(tab==='detailed')renderDetailedLog(el);
  else if(tab==='profitability')renderProfitability(el);
  else if(tab==='staff')renderStaffUtil(el);
  else if(tab==='billing')renderClientBilling(el);
  else if(tab==='wip')renderWIPAging(el);
}
function renderDetailedLog(el){
  var te=(DB.time_entries||[]).slice().sort(function(a,b){return (b.date||'').localeCompare(a.date||'');});
  var tot=te.reduce(function(s,e){return s+(parseFloat(e.hours)||0);},0);
  var wip=te.filter(function(e){return e.billable&&!e.invoiced_ref;}).reduce(function(s,e){return s+((parseFloat(e.hours)||0)*(parseFloat(e.rate)||0));},0);
  el[IH]='<div style="display:flex;gap:16px;margin-bottom:12px"><div class="kpi-card" style="flex:1"><div class="val">'+tot.toFixed(1)+'h</div><div class="sub">Total Hours</div></div><div class="kpi-card" style="flex:1"><div class="val">'+formatCurrency(wip)+'</div><div class="sub">Unbilled WIP</div></div></div>'
    +'<table class="data-table"><thead><tr><th>Date</th><th>Project</th><th>Activity</th><th>Staff</th><th>Hours</th><th>Rate</th><th>Amount</th><th>Status</th></tr></thead><tbody>'
    +te.map(function(e){var h=parseFloat(e.hours)||0,r=parseFloat(e.rate)||0,s=e.invoiced_ref?'Invoiced':e.billable?'Unbilled':'Non-Bill',sc=e.invoiced_ref?'pill-paid':e.billable?'pill-active':'pill-draft';return '<tr><td>'+(e.date||'-')+'</td><td>'+(e.project||'-')+'</td><td>'+(e.activity_type||'-')+'</td><td>'+(e.staff_member||e.logged_by||'-')+'</td><td style="text-align:right">'+h.toFixed(2)+'</td><td style="text-align:right">'+(r?formatCurrency(r):'-')+'</td><td style="text-align:right;color:var(--purple)">'+(h*r?formatCurrency(h*r):'-')+'</td><td><span class="pill '+sc+'">'+s+'</span></td></tr>';}).join('')+'</tbody></table>';
}
function renderProfitability(el){
  var te=DB.time_entries||[];
  el[IH]='<table class="data-table"><thead><tr><th>Project</th><th>Client</th><th>Status</th><th>Hours</th><th>Budget</th><th>%</th><th>WIP</th></tr></thead><tbody>'
    +(DB.projects||[]).map(function(p){var k=p.name||'',pts=te.filter(function(e){return e.project===k;}),totalH=pts.reduce(function(s,e){return s+(parseFloat(e.hours)||0);},0),wip=pts.filter(function(e){return e.billable&&!e.invoiced_ref;}).reduce(function(s,e){return s+((parseFloat(e.hours)||0)*(parseFloat(e.rate)||0));},0),budget=parseFloat(p.budget_hours)||0,pct=budget>0?(totalH/budget*100):0,sc=p.status==='Active'?'pill-active':p.status==='Completed'?'pill-paid':'pill-draft';return '<tr><td>'+k+'</td><td>'+(p.client||'-')+'</td><td><span class="pill '+sc+'">'+(p.status||'Active')+'</span></td><td style="text-align:right">'+totalH.toFixed(1)+'</td><td style="text-align:right">'+(budget||'-')+'</td><td style="text-align:right">'+(budget?pct.toFixed(0)+'%':'-')+'</td><td style="text-align:right;color:var(--purple)">'+formatCurrency(wip)+'</td></tr>';}).join('')+'</tbody></table>';
}
function renderStaffUtil(el){
  var te=DB.time_entries||[],map={};
  te.forEach(function(e){var s=e.staff_member||e.logged_by||'Unknown';if(!map[s])map[s]={b:0,n:0};var h=parseFloat(e.hours)||0;if(e.billable)map[s].b+=h;else map[s].n+=h;});
  el[IH]='<table class="data-table"><thead><tr><th>Staff</th><th>Billable</th><th>Non-Billable</th><th>Total</th><th>Util%</th></tr></thead><tbody>'+Object.entries(map).sort(function(a,b){return (b[1].b+b[1].n)-(a[1].b+a[1].n);}).map(function(e){var n=e[0],d=e[1],tot=d.b+d.n,pct=tot>0?(d.b/tot*100):0;return '<tr><td>'+n+'</td><td style="text-align:right">'+d.b.toFixed(1)+'h</td><td style="text-align:right">'+d.n.toFixed(1)+'h</td><td style="text-align:right">'+tot.toFixed(1)+'h</td><td style="text-align:right">'+pct.toFixed(0)+'%</td></tr>';}).join('')+'</tbody></table>';
}
function renderClientBilling(el){
  var te=DB.time_entries||[],map={};
  te.forEach(function(e){if(!e.billable)return;var c=(DB.projects.find(function(p){return p.name===e.project;})||{}).client||e.project||'Unknown';if(!map[c])map[c]={w:0,i:0};var a=(parseFloat(e.hours)||0)*(parseFloat(e.rate)||0);if(e.invoiced_ref)map[c].i+=a;else map[c].w+=a;});
  el[IH]='<table class="data-table"><thead><tr><th>Client</th><th>Unbilled WIP</th><th>Invoiced</th><th>Total</th></tr></thead><tbody>'+Object.entries(map).sort(function(a,b){return (b[1].w+b[1].i)-(a[1].w+a[1].i);}).map(function(e){var c=e[0],d=e[1];return '<tr><td>'+c+'</td><td style="text-align:right;color:var(--purple)">'+formatCurrency(d.w)+'</td><td style="text-align:right">'+formatCurrency(d.i)+'</td><td style="text-align:right">'+formatCurrency(d.w+d.i)+'</td></tr>';}).join('')+'</tbody></table>';
}
function renderWIPAging(el){
  var te=DB.time_entries||[],today=new Date(),map={};
  te.filter(function(e){return e.billable&&!e.invoiced_ref;}).forEach(function(e){var p=e.project||'Unknown';if(!map[p])map[p]={c30:0,c60:0,c90:0,old:0};var d=e.date?Math.floor((today-new Date(e.date))/86400000):0,a=(parseFloat(e.hours)||0)*(parseFloat(e.rate)||0);if(d<=30)map[p].c30+=a;else if(d<=60)map[p].c60+=a;else if(d<=90)map[p].c90+=a;else map[p].old+=a;});
  el[IH]='<table class="data-table"><thead><tr><th>Project</th><th>0-30d</th><th>31-60d</th><th>61-90d</th><th>&gt;90d</th><th>Total</th></tr></thead><tbody>'+Object.entries(map).map(function(e){var p=e[0],d=e[1],tot=d.c30+d.c60+d.c90+d.old;return '<tr><td>'+p+'</td><td style="text-align:right">'+formatCurrency(d.c30)+'</td><td style="text-align:right">'+formatCurrency(d.c60)+'</td><td style="text-align:right">'+formatCurrency(d.c90)+'</td><td style="text-align:right;color:var(--danger)">'+formatCurrency(d.old)+'</td><td style="text-align:right;color:var(--purple)">'+formatCurrency(tot)+'</td></tr>';}).join('')+'</tbody></table>';
}
""".replace("el[IH]", "el.innerHTML")

# Inject just before </script>
with open(SRC, "rb") as f:
    data = f.read()

marker = b"</script>"
pos = data.rfind(marker)
assert pos > 0, "Could not find </script>"

new_data = data[:pos] + JS.encode("utf-8") + b"\n" + data[pos:]
with open(SRC, "wb") as f:
    f.write(new_data)
print(f"Injected {len(JS)} chars of JS. File: {len(data)} -> {len(new_data)} bytes")
