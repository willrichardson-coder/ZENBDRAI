#!/usr/bin/env python3
"""Save the capped, source-linked research packs produced from Slack recommendations."""
import argparse
import json
import sys
from datetime import datetime

from app import connect, init_db, save_research_record


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='JSON file containing a {"research": [...]} payload.')
    parser.add_argument('--max-records', type=int, default=3, help='Safety cap for one automated audit run.')
    args=parser.parse_args()
    try:
        with open(args.input,encoding='utf-8') as handle: payload=json.load(handle)
        records=payload.get('research') if isinstance(payload,dict) else None
        if not isinstance(records,list) or not records: raise ValueError('Input must contain a non-empty research list.')
        if len(records) > max(1,args.max_records): raise ValueError(f'Refusing more than {max(1,args.max_records)} research records in one run.')
        init_db(); db=connect(); now=datetime.now().isoformat(timespec='seconds'); saved=[]
        try:
            for record in records:
                account_id=str(record.get('account_id') or '').strip()
                recommendation_id=record.get('recommendation_id')
                recommendation=db.execute('SELECT * FROM slack_recommendations WHERE id=?',(recommendation_id,)).fetchone()
                if not recommendation or recommendation['account_id'] != account_id or recommendation['status'] != 'Ready for research':
                    raise ValueError('Each research pack must reference one ready, exact-account Slack recommendation.')
                save_research_record(db,account_id,record,now)
                db.execute("UPDATE slack_recommendations SET status='Research complete',resolution_note=?,updated_at=? WHERE id=?",
                           ('Source-linked account research and an outreach plan were saved.',now,recommendation_id))
                saved.append({'account_id':account_id,'recommendation_id':recommendation_id})
            db.commit(); print(json.dumps({'ok':True,'saved':saved}))
        except Exception:
            db.rollback(); raise
        finally:
            db.close()
    except Exception as error:
        print(json.dumps({'ok':False,'error':str(error)})); sys.exit(1)


if __name__ == '__main__':
    main()
