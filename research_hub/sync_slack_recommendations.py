#!/usr/bin/env python3
"""Store exact, AE-owned Slack account recommendations for the local Research Hub."""
import argparse
import json
import sys
from datetime import date, datetime

from app import connect, init_db, slack_audit_state


def text(value):
    return str(value or '').strip()


def exact_account(db, account_name):
    rows=db.execute('SELECT id,name,owner FROM accounts WHERE lower(name)=lower(?)',(account_name,)).fetchall()
    return rows[0] if len(rows) == 1 else None


def current_research(db, account_id):
    row=db.execute('''SELECT version_date,verified_facts,source_links FROM research_versions
                    WHERE account_id=? ORDER BY version_date DESC,id DESC LIMIT 1''',(account_id,)).fetchone()
    if not row or not text(row['verified_facts']) or not text(row['source_links']): return False
    try: return (date.today()-date.fromisoformat(text(row['version_date'])[:10])).days <= 90
    except ValueError: return False


def ingest_recommendations(db, recommendations, scanned_at=None):
    now=datetime.now().isoformat(timespec='seconds')
    outcome={'received':0,'inserted':0,'already_recorded':0,'ready_for_research':[],
             'unresolved':0,'owner_mismatch':0}
    for item in recommendations:
        account_name=text(item.get('account_name'))
        ae_name=text(item.get('ae_name'))
        ae_slack_user_id=text(item.get('ae_slack_user_id'))
        channel_id=text(item.get('channel_id'))
        message_ts=text(item.get('message_ts'))
        message_text=text(item.get('message_text'))
        recommendation_type=text(item.get('recommendation_type')) or 'Guidance'
        if not all((account_name,ae_name,ae_slack_user_id,channel_id,message_ts,message_text)):
            raise ValueError('Each recommendation needs account_name, AE identity, channel, timestamp, and message text.')
        outcome['received']+=1
        source_key=f'{ae_slack_user_id}:{channel_id}:{message_ts}'
        account=exact_account(db,account_name)
        account_id=None; status='Needs exact account match'; resolution='No exact case-insensitive account-name match in the local CSV universe.'
        if account:
            account_id=account['id']
            if text(account['owner']).casefold() == ae_name.casefold():
                if recommendation_type.casefold() != 'refresh' and current_research(db,account_id):
                    status='Current research available'; resolution='Exact account and owner match. Source-linked research is less than 90 days old.'
                else:
                    status='Ready for research'; resolution='Exact account and current local owner match.'
            else:
                status='Needs ownership review'; resolution=f"Local owner is {text(account['owner']) or 'UNVERIFIED'}, not {ae_name}."
        cursor=db.execute('''INSERT INTO slack_recommendations
          (source_key,account_id,account_name_raw,ae_name,ae_slack_user_id,channel_id,message_ts,message_text,contacts_mentioned,recommendation_type,status,resolution_note,source_url,received_at,created_at,updated_at)
          VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(source_key) DO NOTHING''',
          (source_key,account_id,account_name,ae_name,ae_slack_user_id,channel_id,message_ts,message_text,
           text(item.get('contacts_mentioned')),recommendation_type,status,resolution,text(item.get('source_url')),
           text(item.get('received_at')) or now,now,now))
        if not cursor.rowcount:
            outcome['already_recorded']+=1; continue
        outcome['inserted']+=1
        if status == 'Ready for research':
            outcome['ready_for_research'].append({'recommendation_id':cursor.lastrowid,'account_id':account_id,
                                                  'account_name':account['name'],'ae_name':ae_name,
                                                  'contacts_mentioned':text(item.get('contacts_mentioned'))})
        elif status == 'Needs ownership review':
            outcome['owner_mismatch']+=1
        else:
            outcome['unresolved']+=1
    if scanned_at:
        db.execute("INSERT INTO slack_audit_state(state_key,state_value,updated_at) VALUES ('last_successful_slack_at',?,?) ON CONFLICT(state_key) DO UPDATE SET state_value=excluded.state_value,updated_at=excluded.updated_at",(text(scanned_at),now))
    return outcome


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input', help='JSON file containing {"recommendations": [...], "scanned_at": "..."}.')
    parser.add_argument('--state', action='store_true', help='Print the latest completed Slack audit timestamp.')
    args=parser.parse_args()
    init_db(); db=connect()
    try:
        if args.state:
            print(json.dumps({'last_successful_slack_at':slack_audit_state(db)})); return
        if not args.input: parser.error('Use --input or --state.')
        with open(args.input,encoding='utf-8') as handle: payload=json.load(handle)
        recommendations=payload.get('recommendations') if isinstance(payload,dict) else None
        if not isinstance(recommendations,list): raise ValueError('Input must contain a recommendations list.')
        result=ingest_recommendations(db,recommendations,payload.get('scanned_at'))
        db.commit(); print(json.dumps({'ok':True,**result}))
    except Exception as error:
        db.rollback(); print(json.dumps({'ok':False,'error':str(error)})); sys.exit(1)
    finally:
        db.close()


if __name__ == '__main__':
    main()
