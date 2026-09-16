#!/usr/bin/env python3
import csv, glob, json, os, sqlite3
from datetime import date, datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, unquote

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, '..'))
DATA_ROOT = os.environ.get('RESEARCH_HUB_DATA_DIR', os.path.join(REPO, '08_Working_Accounts', 'research_hub', 'data'))
DB = os.path.join(DATA_ROOT, 'research_hub.sqlite3')
CSV_FILES = [
    '/Users/will.richardson/Downloads/report1787338646698.csv',
    '/Users/will.richardson/Downloads/report1787338765805.csv',
    '/Users/will.richardson/Downloads/report1787338842628.csv',
    '/Users/will.richardson/Downloads/report1787338891667.csv',
    '/Users/will.richardson/Downloads/report1787338939344.csv',
]
INDUSTRY_RESEARCH_FILE = os.path.join(DATA_ROOT, 'industry_research.json')

def connect():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA foreign_keys = ON')
    return db

def init_db():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    db = connect()
    db.executescript('''
    CREATE TABLE IF NOT EXISTS accounts (
      id TEXT PRIMARY KEY, name TEXT NOT NULL, owner TEXT, website TEXT,
      arr_currency TEXT, arr REAL, prospecting_tier TEXT, last_activity TEXT,
      buying_stage TEXT, industry TEXT, sub_industry TEXT, intent_score TEXT,
      market_priority TEXT, employee_count TEXT, assigned_rep TEXT,
      assigned_territory TEXT, source_file TEXT, imported_at TEXT NOT NULL,
      research_status TEXT NOT NULL DEFAULT 'Not researched', researched_on TEXT,
      refresh_after TEXT, suppression_note TEXT, updated_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS research_versions (
      id INTEGER PRIMARY KEY AUTOINCREMENT, account_id TEXT NOT NULL,
      version_date TEXT NOT NULL, title TEXT, verified_facts TEXT,
      inferences TEXT, unknowns TEXT, signal_map TEXT, source_links TEXT,
      notes TEXT, created_at TEXT NOT NULL,
      FOREIGN KEY(account_id) REFERENCES accounts(id) ON DELETE CASCADE
    );
    CREATE TABLE IF NOT EXISTS contacts (
      id INTEGER PRIMARY KEY AUTOINCREMENT, account_id TEXT NOT NULL,
      name TEXT NOT NULL, title TEXT, linkedin_url TEXT, email TEXT,
      function TEXT, tenure TEXT, relevant_language TEXT, signal_connection TEXT,
      confidence TEXT, status TEXT NOT NULL DEFAULT 'Identified', notes TEXT,
      created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
      FOREIGN KEY(account_id) REFERENCES accounts(id) ON DELETE CASCADE
    );
    CREATE TABLE IF NOT EXISTS drafts (
      id INTEGER PRIMARY KEY AUTOINCREMENT, contact_id INTEGER NOT NULL,
      draft_type TEXT NOT NULL, version_date TEXT NOT NULL, subject TEXT,
      body TEXT, status TEXT NOT NULL DEFAULT 'Draft', created_at TEXT NOT NULL,
      FOREIGN KEY(contact_id) REFERENCES contacts(id) ON DELETE CASCADE
    );
    CREATE TABLE IF NOT EXISTS industry_research (
      industry TEXT PRIMARY KEY, account_count INTEGER NOT NULL DEFAULT 0,
      version_date TEXT NOT NULL, summary TEXT, trends TEXT,
      outreach_angles TEXT, questions TEXT, source_links TEXT,
      research_status TEXT NOT NULL DEFAULT 'Current', refresh_after TEXT,
      updated_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS industry_refresh_jobs (
      id INTEGER PRIMARY KEY AUTOINCREMENT, scope TEXT NOT NULL,
      requested_at TEXT NOT NULL, status TEXT NOT NULL, detail TEXT
    );
    CREATE INDEX IF NOT EXISTS idx_accounts_owner ON accounts(owner);
    CREATE INDEX IF NOT EXISTS idx_accounts_status ON accounts(research_status);
    CREATE INDEX IF NOT EXISTS idx_contacts_account ON contacts(account_id);
    CREATE INDEX IF NOT EXISTS idx_drafts_contact ON drafts(contact_id);
    ''')
    db.commit(); db.close()

def import_csvs():
    init_db(); db = connect(); now = datetime.now().isoformat(timespec='seconds')
    count = 0
    for path in CSV_FILES:
        if not os.path.exists(path): continue
        with open(path, newline='', encoding='latin-1') as fh:
            for row in csv.DictReader(fh):
                account_id = row['API Id'].strip()
                values = (
                    account_id, row['Account Name'].strip(), row['Account Owner'].strip(),
                    '', row['Account ARR Currency'].strip(), row['Account ARR'].strip() or None,
                    row['AE Prospecting Tier'].strip(), row['Last Activity'].strip(),
                    row['Buying Stage - 6sense'].strip(), row['Industry'].strip(),
                    row['Sub-Industry'].strip(), row['Intent Score - 6sense'].strip(),
                    row['Market Priority'].strip(), row['Employee Count'].strip(),
                    row['SDR/BDR Assigned'].strip(), row['Assigned Territory'].strip(),
                    os.path.basename(path), now, now)
                db.execute('''INSERT INTO accounts
                  (id,name,owner,website,arr_currency,arr,prospecting_tier,last_activity,
                   buying_stage,industry,sub_industry,intent_score,market_priority,
                   employee_count,assigned_rep,assigned_territory,source_file,imported_at,updated_at)
                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                  ON CONFLICT(id) DO UPDATE SET name=excluded.name, owner=excluded.owner,
                   arr_currency=excluded.arr_currency, arr=excluded.arr, prospecting_tier=excluded.prospecting_tier,
                   last_activity=excluded.last_activity, buying_stage=excluded.buying_stage,
                   industry=excluded.industry, sub_industry=excluded.sub_industry,
                   intent_score=excluded.intent_score, market_priority=excluded.market_priority,
                   employee_count=excluded.employee_count, assigned_rep=excluded.assigned_rep,
                   assigned_territory=excluded.assigned_territory, source_file=excluded.source_file,
                   updated_at=excluded.updated_at''', values)
                count += 1
    db.commit(); db.close(); return count

def seed_industry_research():
    if not os.path.exists(INDUSTRY_RESEARCH_FILE): return 0
    try:
        items=json.load(open(INDUSTRY_RESEARCH_FILE,encoding='utf-8'))
    except (OSError, ValueError):
        return 0
    db=connect(); now=datetime.now().isoformat(timespec='seconds'); count=0
    for item in items:
        n=db.execute('SELECT COUNT(*) FROM accounts WHERE industry=?',(item['industry'],)).fetchone()[0]
        values=(n,item['summary'],item['trends'],item['outreach_angles'],item['questions'],item['sources'],now,item['industry'])
        if db.execute('SELECT 1 FROM industry_research WHERE industry=?',(item['industry'],)).fetchone():
            db.execute('UPDATE industry_research SET account_count=?,summary=?,trends=?,outreach_angles=?,questions=?,source_links=?,updated_at=? WHERE industry=?',values)
        else:
            db.execute('INSERT INTO industry_research(industry,account_count,version_date,summary,trends,outreach_angles,questions,source_links,research_status,refresh_after,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)',(item['industry'],n,'2026-09-04',item['summary'],item['trends'],item['outreach_angles'],item['questions'],item['sources'],'Current','2026-12-03',now)); count+=1
    db.commit(); db.close(); return count

def rows_to_dict(rows): return [dict(r) for r in rows]

def json_body(handler):
    length = int(handler.headers.get('Content-Length', '0'))
    return json.loads(handler.rfile.read(length) or b'{}')

def numeric(value, maximum=100):
    try:
        return max(0, min(maximum, int(float(value or 0))))
    except (TypeError, ValueError):
        return 0

def market_priority_points(value, maximum):
    return {'A': maximum, 'B': round(maximum * .7), 'C': round(maximum * .4), 'D': round(maximum * .1)}.get((value or '').strip().upper(), 0)

def stage_points(value, points):
    return {'Purchase': points, 'Decision': round(points * .9), 'Consideration': round(points * .6), 'Target': round(points * .4), 'Awareness': round(points * .2)}.get((value or '').strip(), 0)

def parse_iso_day(value):
    try:
        return date.fromisoformat((value or '')[:10])
    except (TypeError, ValueError):
        return None

def explicit_hold(note):
    text = (note or '').strip().lower()
    return any(phrase in text for phrase in ('do not contact', 'suppress', 'opt out', 'active opportunity', 'duplicate record', 'exclude from outreach'))

def priority_item(account, latest_research, contact_count, queue_name):
    item = dict(account)
    today = date.today()
    reasons, holds, gaps = [], [], []
    if not (item.get('owner') or '').strip(): holds.append('Owner is missing')
    if explicit_hold(item.get('suppression_note')): holds.append('Explicit outreach hold: ' + item['suppression_note'].strip())
    research_date = parse_iso_day(latest_research.get('version_date') if latest_research else '')
    source_linked = bool(latest_research and (latest_research.get('verified_facts') or '').strip() and (latest_research.get('source_links') or '').strip())
    freshness_days = (today - research_date).days if research_date else None
    if queue_name == 'work':
        if not source_linked: gaps.append('Needs source-linked account research')
        elif freshness_days is None or freshness_days > 90: gaps.append('Account research needs refresh')
        if (item.get('id') or '').startswith('UNVERIFIED:'): gaps.append('CRM account ID is unverified')
        score = 0
        if not holds and not gaps:
            score += 35; reasons.append('Source-linked account research +35')
            recency = 25 if freshness_days <= 30 else 16 if freshness_days <= 60 else 8
            score += recency; reasons.append(f'Research {freshness_days} days old +{recency}')
            priority = market_priority_points(item.get('market_priority'), 20)
            score += priority
            if priority: reasons.append(f'Priority {item.get("market_priority")} +{priority}')
            intent = round(numeric(item.get('intent_score')) / 10)
            score += intent
            if intent: reasons.append(f'CSV intent {numeric(item.get("intent_score"))} +{intent}')
            coverage = 10 if contact_count >= 2 else 5 if contact_count == 1 else 0
            score += coverage
            reasons.append('Contact coverage +' + str(coverage) if coverage else 'No contact coverage')
    else:
        score = 0
        priority = market_priority_points(item.get('market_priority'), 30)
        score += priority
        if priority: reasons.append(f'Priority {item.get("market_priority")} +{priority}')
        intent = round(numeric(item.get('intent_score')) / 4)
        score += intent
        if intent: reasons.append(f'CSV intent {numeric(item.get("intent_score"))} +{intent}')
        stage = stage_points(item.get('buying_stage'), 20)
        score += stage
        if stage: reasons.append(f'{item.get("buying_stage")} stage +{stage}')
        refresh_day = parse_iso_day(item.get('refresh_after'))
        research_gap = 25 if item.get('research_status') != 'Researched' else 15 if refresh_day and refresh_day <= today else 8 if refresh_day and refresh_day <= today + timedelta(days=14) else 0
        score += research_gap
        reasons.append('No account research +25' if item.get('research_status') != 'Researched' else ('Research refresh due +' + str(research_gap) if research_gap else 'Research is current'))
    item['priority_score'] = score
    item['priority_reasons'] = reasons
    item['priority_holds'] = holds
    item['priority_gaps'] = gaps
    item['contact_count'] = contact_count
    item['priority_queue'] = queue_name
    item['source_linked_research'] = source_linked
    return item

def queue_filters(params):
    return {
        'search': params.get('search', [''])[0].strip().lower(),
        'owner': params.get('owner', [''])[0],
        'status': params.get('status', [''])[0],
        'industry': params.get('industry', [''])[0]
    }

def matches_queue_filters(item, filters):
    if filters['search']:
        haystack = ' '.join(str(item.get(field) or '') for field in ('name', 'id', 'industry')).lower()
        if filters['search'] not in haystack: return False
    return (not filters['owner'] or item.get('owner') == filters['owner']) and (not filters['status'] or item.get('research_status') == filters['status']) and (not filters['industry'] or item.get('industry') == filters['industry'])

def build_priority_queue(params):
    from urllib.parse import parse_qs
    filters = queue_filters(params)
    queue_name = params.get('queue', ['research'])[0]
    if queue_name not in ('research', 'work'): queue_name = 'research'
    try:
        limit = max(1, min(24, int(params.get('limit', ['12'])[0])))
        offset = max(0, int(params.get('offset', ['0'])[0]))
    except ValueError:
        limit, offset = 12, 0
    db = connect()
    accounts = rows_to_dict(db.execute('SELECT * FROM accounts'))
    research = {}
    for row in rows_to_dict(db.execute('SELECT * FROM research_versions ORDER BY account_id, version_date DESC, id DESC')):
        research.setdefault(row['account_id'], row)
    contact_counts = {row['account_id']: row['count'] for row in rows_to_dict(db.execute('SELECT account_id, COUNT(*) count FROM contacts GROUP BY account_id'))}
    db.close()
    all_items = [priority_item(account, research.get(account['id']), contact_counts.get(account['id'], 0), queue_name) for account in accounts]
    filtered = [item for item in all_items if matches_queue_filters(item, filters)]
    held_count = sum(bool(item['priority_holds']) for item in filtered)
    not_ready_count = sum(bool(item['priority_gaps']) for item in filtered if not item['priority_holds'])
    eligible = [item for item in filtered if not item['priority_holds'] and (queue_name != 'work' or not item['priority_gaps'])]
    eligible.sort(key=lambda item: (-item['priority_score'], item['name'].lower()))
    if queue_name == 'work':
        subtitle = 'Requires dated, source-linked account research. CSV intent and stage only rank the verified work.'
        empty_message = 'No accounts clear the evidence gate. Build or refresh account-specific research before outreach.'
    else:
        subtitle = 'Ranks research work using CSV priority, intent, and stage. These are screening signals, not proof of fit or pain.'
        empty_message = 'No eligible accounts match these filters.'
    return {'items': eligible[offset:offset + limit], 'total': len(eligible), 'held_total': held_count, 'not_ready_total': not_ready_count, 'limit': limit, 'offset': offset, 'queue': queue_name, 'subtitle': subtitle, 'empty_message': empty_message}

class Handler(BaseHTTPRequestHandler):
    def send_json(self, payload, code=200):
        body = json.dumps(payload).encode()
        self.send_response(code); self.send_header('Content-Type','application/json')
        self.send_header('Content-Length',str(len(body))); self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        parsed = urlparse(self.path); path = parsed.path
        if path == '/api/stats':
            db=connect(); today=date.today().isoformat(); due=(date.today()+timedelta(days=14)).isoformat()
            out={'total':db.execute('SELECT COUNT(*) FROM accounts').fetchone()[0],
                 'researched':db.execute("SELECT COUNT(*) FROM accounts WHERE research_status='Researched'").fetchone()[0],
                 'needs_refresh':db.execute("SELECT COUNT(*) FROM accounts WHERE refresh_after IS NOT NULL AND refresh_after<=?",(today,)).fetchone()[0],
                 'due_next_14':db.execute("SELECT COUNT(*) FROM accounts WHERE refresh_after IS NOT NULL AND refresh_after<=?",(due,)).fetchone()[0],
                 'unverified_crm_ids':db.execute("SELECT COUNT(*) FROM accounts WHERE id LIKE 'UNVERIFIED:%'").fetchone()[0],
                 'owners':rows_to_dict(db.execute('SELECT owner,COUNT(*) count FROM accounts GROUP BY owner ORDER BY owner')),
                 'industries':db.execute('SELECT COUNT(*) FROM industry_research').fetchone()[0]}; db.close(); return self.send_json(out)
        if path == '/api/industries':
            db=connect(); data=rows_to_dict(db.execute('SELECT * FROM industry_research ORDER BY account_count DESC,industry')); db.close(); return self.send_json(data)
        if path == '/api/industry-refresh-jobs':
            db=connect(); data=rows_to_dict(db.execute('SELECT * FROM industry_refresh_jobs ORDER BY id DESC LIMIT 20')); db.close(); return self.send_json(data)
        if path == '/api/account-queue':
            from urllib.parse import parse_qs
            return self.send_json(build_priority_queue(parse_qs(urlparse(self.path).query)))
        if path == '/api/accounts':
            q = urlparse(self.path).query; from urllib.parse import parse_qs; p=parse_qs(q)
            search=p.get('search',[''])[0].strip(); owner=p.get('owner',[''])[0]; status=p.get('status',[''])[0]; industry=p.get('industry',[''])[0]
            sql='SELECT * FROM accounts WHERE 1=1'; args=[]
            if search: sql += ' AND (name LIKE ? OR id LIKE ? OR industry LIKE ?)'; args += [f'%{search}%']*3
            if owner: sql += ' AND owner=?'; args.append(owner)
            if status: sql += ' AND research_status=?'; args.append(status)
            if industry: sql += ' AND industry=?'; args.append(industry)
            sql += ' ORDER BY owner,name'; db=connect(); data=rows_to_dict(db.execute(sql,args)); db.close(); return self.send_json(data)
        if path.startswith('/api/accounts/'):
            account_id=unquote(path.split('/')[3]); db=connect(); account=db.execute('SELECT * FROM accounts WHERE id=?',(account_id,)).fetchone()
            if not account: db.close(); return self.send_json({'error':'Account not found'},404)
            research=rows_to_dict(db.execute('SELECT * FROM research_versions WHERE account_id=? ORDER BY version_date DESC,id DESC',(account_id,)))
            contacts=rows_to_dict(db.execute('SELECT * FROM contacts WHERE account_id=? ORDER BY name',(account_id,)))
            for c in contacts: c['drafts']=rows_to_dict(db.execute('SELECT * FROM drafts WHERE contact_id=? ORDER BY version_date DESC,id DESC',(c['id'],)))
            db.close(); return self.send_json({'account':dict(account),'research':research,'contacts':contacts})
        if path == '/' or path == '/index.html':
            return self.serve(os.path.join(ROOT,'static','index.html'),'text/html; charset=utf-8')
        if path.startswith('/static/'):
            full=os.path.join(ROOT,path[1:]); types={'.js':'text/javascript','.css':'text/css','.html':'text/html'}
            return self.serve(full,types.get(os.path.splitext(full)[1],'application/octet-stream'))
        return self.send_json({'error':'Not found'},404)
    def serve(self, path, content_type):
        try: body=open(path,'rb').read()
        except FileNotFoundError: return self.send_json({'error':'Not found'},404)
        self.send_response(200); self.send_header('Content-Type',content_type); self.send_header('Content-Length',str(len(body))); self.end_headers(); self.wfile.write(body)
    def do_POST(self):
        path=urlparse(self.path).path; data=json_body(self); now=datetime.now().isoformat(timespec='seconds'); db=connect()
        try:
            if path == '/api/industry-research/refresh':
                scope=data.get('industry') or 'ALL INDUSTRIES'; targets=[scope] if scope != 'ALL INDUSTRIES' else [r[0] for r in db.execute('SELECT industry FROM industry_research ORDER BY industry')]
                stamp=now; db.execute('INSERT INTO industry_refresh_jobs(scope,requested_at,status,detail) VALUES (?,?,?,?)',(scope,stamp,'Requested',f'Refresh requested for {len(targets)} industry record(s). Re-run the live research pass, then save the dated result.'))
                db.execute("UPDATE industry_research SET research_status='Refresh requested',updated_at=? WHERE industry IN (%s)" % ','.join('?'*len(targets)),[stamp]+targets)
            elif path.startswith('/api/accounts/') and path.endswith('/research'):
                aid=unquote(path.split('/')[3]); d=data; vdate=d.get('version_date') or date.today().isoformat()
                db.execute('INSERT INTO research_versions(account_id,version_date,title,verified_facts,inferences,unknowns,signal_map,source_links,notes,created_at) VALUES (?,?,?,?,?,?,?,?,?,?)',(aid,vdate,d.get('title',''),d.get('verified_facts',''),d.get('inferences',''),d.get('unknowns',''),d.get('signal_map',''),d.get('source_links',''),d.get('notes',''),now))
                refresh=(date.fromisoformat(vdate)+timedelta(days=90)).isoformat()
                db.execute("UPDATE accounts SET research_status='Researched',researched_on=?,refresh_after=?,updated_at=? WHERE id=?",(vdate,refresh,now,aid))
            elif path.startswith('/api/accounts/') and path.endswith('/contacts'):
                aid=unquote(path.split('/')[3]); d=data
                db.execute('INSERT INTO contacts(account_id,name,title,linkedin_url,email,function,tenure,relevant_language,signal_connection,confidence,status,notes,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(aid,d.get('name',''),d.get('title',''),d.get('linkedin_url',''),d.get('email',''),d.get('function',''),d.get('tenure',''),d.get('relevant_language',''),d.get('signal_connection',''),d.get('confidence',''),d.get('status','Identified'),d.get('notes',''),now,now))
            elif path.startswith('/api/contacts/') and path.endswith('/drafts'):
                cid=unquote(path.split('/')[3]); d=data
                db.execute('INSERT INTO drafts(contact_id,draft_type,version_date,subject,body,status,created_at) VALUES (?,?,?,?,?,?,?)',(cid,d.get('draft_type','Email 1'),d.get('version_date') or date.today().isoformat(),d.get('subject',''),d.get('body',''),d.get('status','Draft'),now))
            else: db.close(); return self.send_json({'error':'Not found'},404)
            db.commit(); db.close(); return self.send_json({'ok':True})
        except Exception as e:
            db.rollback(); db.close(); return self.send_json({'error':str(e)},400)
    def log_message(self, *_): pass

if __name__ == '__main__':
    import_csvs(); seed_industry_research(); port=int(os.environ.get('RESEARCH_HUB_PORT','8765'))
    print(f'Research Hub: http://127.0.0.1:{port}')
    ThreadingHTTPServer(('127.0.0.1',port),Handler).serve_forever()
