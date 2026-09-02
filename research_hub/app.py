#!/usr/bin/env python3
import csv, glob, json, os, sqlite3
from datetime import date, datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

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

def rows_to_dict(rows): return [dict(r) for r in rows]

def json_body(handler):
    length = int(handler.headers.get('Content-Length', '0'))
    return json.loads(handler.rfile.read(length) or b'{}')

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
                 'owners':rows_to_dict(db.execute('SELECT owner,COUNT(*) count FROM accounts GROUP BY owner ORDER BY owner'))}; db.close(); return self.send_json(out)
        if path == '/api/accounts':
            q = urlparse(self.path).query; from urllib.parse import parse_qs; p=parse_qs(q)
            search=p.get('search',[''])[0].strip(); owner=p.get('owner',[''])[0]; status=p.get('status',[''])[0]
            sql='SELECT * FROM accounts WHERE 1=1'; args=[]
            if search: sql += ' AND (name LIKE ? OR id LIKE ? OR industry LIKE ?)'; args += [f'%{search}%']*3
            if owner: sql += ' AND owner=?'; args.append(owner)
            if status: sql += ' AND research_status=?'; args.append(status)
            sql += ' ORDER BY owner,name'; db=connect(); data=rows_to_dict(db.execute(sql,args)); db.close(); return self.send_json(data)
        if path.startswith('/api/accounts/'):
            account_id=path.split('/')[3]; db=connect(); account=db.execute('SELECT * FROM accounts WHERE id=?',(account_id,)).fetchone()
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
            if path.startswith('/api/accounts/') and path.endswith('/research'):
                aid=path.split('/')[3]; d=data; vdate=d.get('version_date') or date.today().isoformat()
                db.execute('INSERT INTO research_versions(account_id,version_date,title,verified_facts,inferences,unknowns,signal_map,source_links,notes,created_at) VALUES (?,?,?,?,?,?,?,?,?,?)',(aid,vdate,d.get('title',''),d.get('verified_facts',''),d.get('inferences',''),d.get('unknowns',''),d.get('signal_map',''),d.get('source_links',''),d.get('notes',''),now))
                refresh=(date.fromisoformat(vdate)+timedelta(days=90)).isoformat()
                db.execute("UPDATE accounts SET research_status='Researched',researched_on=?,refresh_after=?,updated_at=? WHERE id=?",(vdate,refresh,now,aid))
            elif path.startswith('/api/accounts/') and path.endswith('/contacts'):
                aid=path.split('/')[3]; d=data
                db.execute('INSERT INTO contacts(account_id,name,title,linkedin_url,email,function,tenure,relevant_language,signal_connection,confidence,status,notes,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(aid,d.get('name',''),d.get('title',''),d.get('linkedin_url',''),d.get('email',''),d.get('function',''),d.get('tenure',''),d.get('relevant_language',''),d.get('signal_connection',''),d.get('confidence',''),d.get('status','Identified'),d.get('notes',''),now,now))
            elif path.startswith('/api/contacts/') and path.endswith('/drafts'):
                cid=path.split('/')[3]; d=data
                db.execute('INSERT INTO drafts(contact_id,draft_type,version_date,subject,body,status,created_at) VALUES (?,?,?,?,?,?,?)',(cid,d.get('draft_type','Email 1'),d.get('version_date') or date.today().isoformat(),d.get('subject',''),d.get('body',''),d.get('status','Draft'),now))
            else: db.close(); return self.send_json({'error':'Not found'},404)
            db.commit(); db.close(); return self.send_json({'ok':True})
        except Exception as e:
            db.rollback(); db.close(); return self.send_json({'error':str(e)},400)
    def log_message(self, *_): pass

if __name__ == '__main__':
    import_csvs(); port=int(os.environ.get('RESEARCH_HUB_PORT','8765'))
    print(f'Research Hub: http://127.0.0.1:{port}')
    ThreadingHTTPServer(('127.0.0.1',port),Handler).serve_forever()
