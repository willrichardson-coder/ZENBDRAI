#!/usr/bin/env python3
"""Idempotently store normalized Gmail Sent records in the local Research Hub."""
import argparse
import json
import sys

from app import connect, ingest_sent_messages, init_db, sent_audit_state


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input', help='JSON file containing a {"messages": [...]} payload.')
    parser.add_argument('--state', action='store_true', help='Print the most recent successfully recorded sent timestamp.')
    args=parser.parse_args()
    init_db(); db=connect()
    try:
        if args.state:
            print(json.dumps({'last_successful_sent_at':sent_audit_state(db)})); return
        if not args.input:
            parser.error('Use --input or --state.')
        with open(args.input,encoding='utf-8') as handle: payload=json.load(handle)
        messages=payload.get('messages') if isinstance(payload,dict) else None
        if not isinstance(messages,list) or not messages: raise ValueError('Input must contain a non-empty messages list.')
        result=ingest_sent_messages(db,messages)
        db.commit(); print(json.dumps({'ok':True,**result}))
    except Exception as error:
        db.rollback(); print(json.dumps({'ok':False,'error':str(error)})); sys.exit(1)
    finally:
        db.close()


if __name__ == '__main__':
    main()
