let selectedIndustry = '';
let selectedAccount = '';
let selectedQueue = 'research';
let industryRows = [];
let queueItems = new Map();
let pageOffset = 0;
const pageSize = 12;

const $ = selector => document.querySelector(selector);
const esc = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
const safeHttpUrl = value => {
  try {
    const url = new URL(value);
    return ['http:', 'https:'].includes(url.protocol) ? url.href : '';
  } catch (_) {
    return '';
  }
};
async function get(url){ return (await fetch(url)).json(); }
async function post(url, data){ return (await fetch(url, {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(data)})).json(); }

function query(){
  const params = new URLSearchParams({search:$('#search').value, owner:$('#owner').value, status:$('#status').value, queue:selectedQueue, limit:pageSize, offset:pageOffset});
  if(selectedIndustry) params.set('industry', selectedIndustry);
  return params;
}

function modeLabel(){ return selectedQueue === 'research' ? 'Research next' : 'Work today'; }

async function loadStats(){
  const stats = await get('/api/stats');
  $('#stats').innerHTML = [['total','Accounts','Active universe'],['researched','Researched','Dated account work'],['timing_signals_last_7','Timing signals','Last 7 days'],['needs_refresh','Need refresh','Past due'],['due_next_14','14 day horizon','Due soon'],['industries','Industries','Market lenses']]
    .map(item => `<article class="stat-card"><span>${esc(item[1])}</span><b>${stats[item[0]]}</b><small>${esc(item[2])}</small></article>`).join('');
  const integrity = $('#dataIntegrity');
  const unresolved = Number(stats.unverified_crm_ids || 0);
  integrity.hidden = !unresolved;
  integrity.textContent = unresolved === 1
    ? 'Data quality: 1 retained legacy account has an unverified CRM ID. It is excluded from Work today.'
    : `Data quality: ${unresolved} retained legacy accounts have unverified CRM IDs. They are excluded from Work today.`;
  const previousOwner = $('#owner').value;
  $('#owner').innerHTML = '<option value="">All AEs</option>' + stats.owners.map(owner => `<option>${esc(owner.owner)}</option>`).join('');
  $('#owner').value = previousOwner;
}

async function loadWeeklyRefresh(){
  const data = await get('/api/weekly-refresh');
  const latest = data.runs[0];
  const summary = latest
    ? `${latest.account_count} reviewed · ${latest.timing_signal_count} timing signal${latest.timing_signal_count === 1 ? '' : 's'} · ${esc(latest.run_date)}`
    : 'No weekly timing refresh has been saved yet.';
  const cards = data.signals.slice(0,4).map(signal => `<article class="timing-card"><div><span class="timing-status">TIMING SIGNAL</span><small>${esc(signal.run_date)}</small></div><h3>${esc(signal.account_name)}</h3><p>${esc(signal.headline)}</p><small>${esc(signal.outreach_implication || 'Review the evidence before outreach.')}</small></article>`).join('');
  $('#weeklyRefresh').innerHTML = `<div class="weekly-refresh-head"><div><p class="eyebrow">SUNDAY TIMING REVIEW</p><h2>What changed since the account brief?</h2><p>${summary}</p></div><span class="count-badge">${data.signals.length} saved signals</span></div>${cards ? `<div class="timing-grid">${cards}</div>` : '<p class="muted timing-empty">The Sunday pass will record source-linked signals, clear no-signal findings, or evidence gaps. It does not replace account research.</p>'}`;
}

async function loadIndustries(){
  industryRows = await get('/api/industries');
  $('#industryCount').textContent = industryRows.length + ' industries';
  $('#industryRadar').innerHTML = industryRows.map((industry, index) => `<button class="radar-card ${selectedIndustry === industry.industry ? 'active' : ''}" data-industry="${esc(industry.industry)}"><span class="radar-rank">${String(index + 1).padStart(2,'0')}</span><strong>${esc(industry.industry)}</strong><small>${industry.account_count} accounts</small><i style="width:${Math.max(8,Math.round(industry.account_count / industryRows[0].account_count * 100))}%"></i></button>`).join('');
  document.querySelectorAll('.radar-card').forEach(button => button.onclick = () => selectIndustry(button.dataset.industry));
  renderIntelligence();
}

function renderIntelligence(){
  const item = industryRows.find(industry => industry.industry === selectedIndustry);
  if(!item){
    $('#intelligence').innerHTML = '<div class="empty-state"><span class="empty-orb">✦</span><p class="eyebrow">SELECT AN INDUSTRY</p><h2>Start with the market signal.</h2><p>Choose an industry to see the account universe, public context, outreach angle, and diagnostic question.</p></div>';
    return;
  }
  $('#intelligence').innerHTML = `<div class="intelligence-head"><div><p class="eyebrow">ACTIVE LENS</p><h2>${esc(item.industry)}</h2><span class="count-badge">${item.account_count} accounts</span></div><button id="refreshSelected" class="ghost-button">Refresh research</button></div><p class="summary">${esc(item.summary)}</p><div class="intel-grid"><div><p class="eyebrow">TREND</p><p>${esc(item.trends)}</p></div><div><p class="eyebrow">OUTREACH ANGLE</p><p>${esc(item.outreach_angles)}</p></div></div><div class="question-card"><p class="eyebrow">DIAGNOSTIC QUESTION</p><p>${esc(item.questions)}</p></div><details class="source-toggle"><summary>View research sources</summary><p>${esc(item.source_links)}</p></details>`;
  $('#refreshSelected').onclick = () => refreshIndustry(item.industry);
}

function renderQueueGuide(data){
  const message = selectedQueue === 'research'
    ? 'CSV priority, intent, and stage decide what to verify first. They do not prove Zendesk fit, customer state, or account pain. The 120 July legacy Drive account templates are reference-only and are not imported here.'
    : 'Only dated, source-linked account research enters this queue. A card can still show missing contact coverage as the next account-work step. The 120 July legacy Drive account templates do not clear this gate.';
  const control = selectedQueue === 'work'
    ? `${data.not_ready_total} record${data.not_ready_total === 1 ? '' : 's'} need evidence or CRM-ID resolution before they can enter Work today.`
    : (data.held_total ? `${data.held_total} record${data.held_total === 1 ? '' : 's'} held from this view for an explicit suppression or missing owner.` : 'No records are held by the available ownership and suppression checks.');
  $('#queueGuide').innerHTML = `<div><p class="eyebrow">HOW TO READ THIS</p><p>${esc(message)}</p></div><div><p class="eyebrow">QUEUE CONTROL</p><p>${esc(control)}</p></div>`;
}

function renderQueueTabs(){
  document.querySelectorAll('.queue-tab').forEach(button => {
    const active = button.dataset.queue === selectedQueue;
    button.classList.toggle('active', active);
    button.setAttribute('aria-selected', String(active));
  });
}

async function loadQueue(){
  const data = await get('/api/account-queue?' + query());
  queueItems = new Map(data.items.map(item => [item.id, item]));
  const start = data.total ? data.offset + 1 : 0;
  const end = Math.min(data.offset + data.limit, data.total);
  $('#queueTitle').textContent = selectedIndustry ? `${modeLabel()} · ${selectedIndustry}` : modeLabel();
  $('#queueSubtitle').textContent = data.total ? `Showing ${start}-${end} of ${data.total} eligible accounts. ${data.subtitle}` : data.empty_message;
  $('#queueCount').textContent = data.total + ' eligible';
  $('#previousPage').disabled = data.offset === 0;
  $('#nextPage').disabled = data.offset + data.limit >= data.total;
  renderQueueTabs();
  renderQueueGuide(data);
  $('#accountQueue').innerHTML = data.items.map(account => `<button class="account-card ${selectedAccount === account.id ? 'active' : ''}" data-id="${esc(account.id)}"><div class="account-card-top"><span class="status-dot ${account.research_status === 'Researched' ? 'done' : ''}"></span><small>${esc(account.owner)}</small><span class="priority">${account.priority_score}</span></div><h3>${esc(account.name)}</h3><p>${esc(account.industry)}</p><div class="account-reason">${esc(account.priority_reasons[0] || 'Needs review')}</div><div class="account-meta"><span>${esc(account.buying_stage || 'Unknown stage')}</span><span>Intent ${esc(account.intent_score || 'Unknown')}</span><span>${account.contact_count} contact${account.contact_count === 1 ? '' : 's'}</span></div></button>`).join('') || `<div class="empty-state queue-empty"><span class="empty-orb">⌕</span><h2>${selectedQueue === 'work' ? 'Evidence gate is working.' : 'No accounts found'}</h2><p>${esc(data.empty_message)}</p></div>`;
  document.querySelectorAll('.account-card').forEach(button => button.onclick = () => loadAccount(button.dataset.id));
}

function selectIndustry(industry){
  selectedIndustry = industry;
  pageOffset = 0;
  loadIndustries();
  loadQueue();
  document.querySelector('.queue-section').scrollIntoView({behavior:'smooth', block:'start'});
}

async function loadAccount(id){
  selectedAccount = id;
  const data = await get('/api/accounts/' + encodeURIComponent(id));
  const account = data.account;
  const priority = queueItems.get(id);
  const reasons = priority ? priority.priority_reasons.map(reason => `<li>${esc(reason)}</li>`).join('') : '<li>Priority details unavailable.</li>';
  const draftCount = data.contacts.reduce((count, contact) => count + contact.drafts.length, 0);
  const sentCount = data.contacts.reduce((count, contact) => count + (Array.isArray(contact.sent_messages) ? contact.sent_messages.length : 0), 0);
  const recommendations = Array.isArray(data.recommendations) ? data.recommendations : [];
  const refreshSignals = Array.isArray(data.refresh_signals) ? data.refresh_signals : [];
  const timingHistory = refreshSignals.length
    ? refreshSignals.map(signal => `<article class="timing-history"><div class="draft-head"><span class="timing-status">${esc(signal.status)}</span><time datetime="${esc(signal.run_date)}">${esc(signal.run_date)}</time></div><b>${esc(signal.headline)}</b><p>${esc(signal.verified_events)}</p>${signal.inference ? `<p class="timing-inference"><b>Inference:</b> ${esc(signal.inference)}</p>` : ''}${signal.outreach_implication ? `<p class="research-plan"><b>Outreach implication:</b> ${esc(signal.outreach_implication)}</p>` : ''}<details class="source-toggle"><summary>View sources</summary><p>${esc(signal.source_links)}</p></details></article>`).join('')
    : '<p class="muted">No weekly timing review saved. This does not make the account brief stale.</p>';
  const slackDirection = recommendations.length
    ? recommendations.map(item => { const sourceUrl=safeHttpUrl(item.source_url); return `<article class="slack-recommendation"><div class="draft-head"><span class="slack-status">${esc(item.status)}</span><span class="draft-type">${esc(item.recommendation_type)}</span><time datetime="${esc(item.received_at)}">${esc(item.received_at)}</time></div><p><b>${esc(item.ae_name)}</b> · ${esc(item.message_text)}</p>${item.contacts_mentioned ? `<p class="recommendation-contacts"><b>Contacts named by AE:</b> ${esc(item.contacts_mentioned)} <span>Unverified until checked.</span></p>` : ''}${item.resolution_note ? `<p class="recommendation-note">${esc(item.resolution_note)}</p>` : ''}${sourceUrl ? `<a class="contact-link" href="${esc(sourceUrl)}" target="_blank" rel="noreferrer">Open Slack source</a>` : ''}</article>`; }).join('')
    : '<p class="muted">No account-specific Slack direction is saved yet.</p>';
  const contactWorkspace = data.contacts.length
    ? data.contacts.map(contact => {
        const contactDetails = [
          contact.function,
          contact.tenure,
          contact.email,
        ].filter(Boolean).map(detail => `<span>${esc(detail)}</span>`).join('');
        const signal = contact.signal_connection
          ? `<p class="contact-signal"><b>Account signal:</b> ${esc(contact.signal_connection)}</p>`
          : '';
        const relevantLanguage = contact.relevant_language
          ? `<p class="contact-language">${esc(contact.relevant_language)}</p>`
          : '';
        const notes = contact.notes
          ? `<p class="contact-notes"><b>Notes:</b> ${esc(contact.notes)}</p>`
          : '';
        const profileUrl = safeHttpUrl(contact.linkedin_url);
        const profile = profileUrl
          ? `<a class="contact-link" href="${esc(profileUrl)}" target="_blank" rel="noreferrer">LinkedIn profile</a>`
          : '';
        const drafts = contact.drafts.length
          ? `<div class="draft-list">${contact.drafts.map(draft => `<article class="draft-card"><div class="draft-head"><span class="draft-type">${esc(draft.draft_type)}</span><span class="draft-status">${esc(draft.status)}</span><time datetime="${esc(draft.version_date)}">${esc(draft.version_date)}</time></div>${draft.subject ? `<p class="draft-subject">${esc(draft.subject)}</p>` : ''}<p class="draft-body">${esc(draft.body || 'No writing saved in this draft.')}</p></article>`).join('')}</div>`
          : '<p class="muted contact-empty">No saved writing for this prospect yet.</p>';
        const sentRecords = Array.isArray(contact.sent_messages) ? contact.sent_messages : [];
        const sentMessages = sentRecords.length
          ? `<div class="sent-list">${sentRecords.map(message => { const sourceUrl=safeHttpUrl(message.source_url); return `<article class="sent-card"><div class="draft-head"><span class="sent-status">Sent</span><time datetime="${esc(message.sent_at)}">${esc(message.sent_at)}</time></div>${message.subject ? `<p class="draft-subject">${esc(message.subject)}</p>` : ''}<p class="draft-body">${esc(message.body_text || 'No plain-text body was available.')}</p>${sourceUrl ? `<a class="contact-link" href="${esc(sourceUrl)}" target="_blank" rel="noreferrer">Open in Gmail</a>` : ''}</article>`; }).join('')}</div>`
          : '';
        return `<article class="contact-card"><div class="contact-head"><div><h3>${esc(contact.name)}</h3><p>${esc(contact.title || 'Title not saved')}</p></div><span class="contact-status">${esc(contact.status || 'Identified')}</span></div>${contactDetails ? `<div class="contact-details">${contactDetails}</div>` : ''}${signal}${relevantLanguage}${notes}${profile}<div class="contact-writing"><p class="eyebrow">SAVED WRITING</p>${drafts}</div>${sentMessages ? `<div class="contact-writing sent-writing"><p class="eyebrow">SENT EMAILS</p>${sentMessages}</div>` : ''}</article>`;
      }).join('')
    : '<div class="contact-empty-state"><p class="muted">No contacts are attached to this account yet. Account research can be saved before contact selection.</p></div>';
  $('#drawerName').textContent = account.name;
  $('#drawerBody').innerHTML = `<div class="drawer-meta"><span>${esc(account.owner || 'Owner not saved')}</span><span>${esc(account.industry || 'Industry not saved')}</span><span>Priority ${esc(account.market_priority || 'Unknown')}</span></div><div class="drawer-stats"><div><small>Queue score</small><b>${priority ? priority.priority_score : 'Unknown'}</b></div><div><small>Intent score</small><b>${esc(account.intent_score || 'Unknown')}</b></div><div><small>Research</small><b>${esc(account.research_status)}</b></div><div><small>Contacts</small><b>${data.contacts.length}</b></div><div><small>Drafts</small><b>${draftCount}</b></div><div><small>Sent</small><b>${sentCount}</b></div></div><div class="drawer-block"><p class="eyebrow">WHY THIS IS HERE</p><ul class="priority-reasons">${reasons}</ul></div><div class="drawer-block"><p class="eyebrow">WEEKLY TIMING REVIEW</p>${timingHistory}</div><div class="drawer-block"><p class="eyebrow">SLACK DIRECTION</p>${slackDirection}</div><div class="drawer-block"><p class="eyebrow">ACCOUNT RESEARCH</p>${data.research.length ? data.research.map(research => `<article><b>${esc(research.title || 'Research')}</b><small>${esc(research.version_date)}</small><p>${esc(research.signal_map || research.notes || 'No signal map saved.')}</p>${research.outreach_plan ? `<p class="research-plan"><b>Outreach plan:</b> ${esc(research.outreach_plan)}</p>` : ''}</article>`).join('') : '<p class="muted">No account research saved yet. Start with the industry question, then verify the account-specific signal.</p>'}</div><div class="drawer-block contact-workspace"><div class="contact-workspace-heading"><div><p class="eyebrow">CONTACTS AND MESSAGING</p><h3>${data.contacts.length} prospect${data.contacts.length === 1 ? '' : 's'} · ${draftCount} saved draft${draftCount === 1 ? '' : 's'} · ${sentCount} sent email${sentCount === 1 ? '' : 's'}</h3></div></div>${contactWorkspace}</div>`;
  $('#accountDrawer').classList.add('open');
  loadQueue();
}

function clearFilters(){
  selectedIndustry = '';
  pageOffset = 0;
  $('#search').value = '';
  $('#owner').value = '';
  $('#status').value = '';
  loadIndustries();
  loadQueue();
}

async function refreshIndustry(industry){
  const response = await post('/api/industry-research/refresh', {industry});
  $('#jobStatus').textContent = response.ok ? 'Refresh requested for ' + industry + '.' : 'Refresh request failed';
  loadIndustries();
}

['search','owner','status'].forEach(id => $('#'+id).oninput = () => { pageOffset = 0; loadQueue(); });
document.querySelectorAll('.queue-tab').forEach(button => button.onclick = () => { selectedQueue = button.dataset.queue; pageOffset = 0; selectedAccount = ''; $('#accountDrawer').classList.remove('open'); loadQueue(); });
$('#clearFilters').onclick = clearFilters;
$('#previousPage').onclick = () => { pageOffset = Math.max(0, pageOffset - pageSize); loadQueue(); };
$('#nextPage').onclick = () => { pageOffset += pageSize; loadQueue(); };
$('#closeDrawer').onclick = () => $('#accountDrawer').classList.remove('open');
$('#refresh').onclick = () => { loadStats(); loadWeeklyRefresh(); loadIndustries(); loadQueue(); };
$('#refreshAll').onclick = () => refreshIndustry('ALL INDUSTRIES');
loadStats();
loadWeeklyRefresh();
loadIndustries();
loadQueue();
