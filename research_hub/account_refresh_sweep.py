#!/usr/bin/env python3
"""Read and save complete weekly timing reviews for source-linked account research."""
import argparse
import json
import sys
from datetime import date, datetime

from app import connect, init_db, rows_to_dict, save_refresh_signal


def eligible_accounts(db):
    return rows_to_dict(db.execute('''SELECT a.id,a.name,a.owner,a.industry,a.website,
      r.version_date,r.verified_facts,r.inferences,r.signal_map,r.source_links,r.outreach_plan
      FROM accounts a
      JOIN research_versions r ON r.id=(
        SELECT latest.id FROM research_versions latest
        WHERE latest.account_id=a.id
        ORDER BY latest.version_date DESC,latest.id DESC LIMIT 1
      )
      WHERE a.research_status='Researched'
      ORDER BY a.name COLLATE NOCASE'''))


def show_eligible():
    db=connect()
    accounts=eligible_accounts(db)
    db.close()
    print(json.dumps({'accounts':accounts,'count':len(accounts)},indent=2))


def show_state():
    db=connect()
    runs=rows_to_dict(db.execute('SELECT * FROM weekly_refresh_runs ORDER BY run_date DESC LIMIT 8'))
    db.close()
    print(json.dumps({'runs':runs},indent=2))


def save_input(path):
    try:
        payload=json.load(open(path,encoding='utf-8'))
    except (OSError,json.JSONDecodeError) as exc:
        raise ValueError(f'Cannot read refresh input: {exc}')
    run_date=str(payload.get('run_date') or date.today().isoformat())
    try:
        date.fromisoformat(run_date)
    except ValueError:
        raise ValueError('run_date must use YYYY-MM-DD.')
    reviews=payload.get('refreshes')
    if not isinstance(reviews,list):
        raise ValueError('Input needs a refreshes list.')
    db=connect()
    expected=eligible_accounts(db)
    expected_ids={row['id'] for row in expected}
    supplied_ids=[str(row.get('account_id') or '').strip() for row in reviews if isinstance(row,dict)]
    if len(supplied_ids)!=len(reviews) or len(set(supplied_ids))!=len(supplied_ids):
        db.close(); raise ValueError('Each refresh needs one unique account_id.')
    missing=sorted(expected_ids-set(supplied_ids))
    unexpected=sorted(set(supplied_ids)-expected_ids)
    if missing or unexpected:
        db.close()
        detail=[]
        if missing: detail.append(f'missing {len(missing)} eligible account(s)')
        if unexpected: detail.append(f'{len(unexpected)} account(s) are not eligible')
        raise ValueError('Refresh coverage is incomplete: ' + '; '.join(detail) + '.')
    now=datetime.now().isoformat(timespec='seconds')
    try:
        db.execute('''INSERT INTO weekly_refresh_runs(run_date,started_at,status,detail)
          VALUES (?,?,?,?) ON CONFLICT(run_date) DO UPDATE SET started_at=excluded.started_at,
          completed_at=NULL,status=excluded.status,detail=excluded.detail''',
          (run_date,now,'Running','Validating complete weekly coverage.'))
        for review in reviews:
            save_refresh_signal(db,review['account_id'],review,run_date,now)
        timing_signals=sum(1 for review in reviews if review.get('status')=='Timing signal')
        db.execute('''UPDATE weekly_refresh_runs SET completed_at=?,status='Completed',
          account_count=?,timing_signal_count=?,detail=? WHERE run_date=?''',
          (now,len(reviews),timing_signals,'Every eligible researched account received one timing review.',run_date))
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
    print(json.dumps({'ok':True,'run_date':run_date,'accounts_reviewed':len(reviews),'timing_signals':timing_signals},indent=2))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--eligible',action='store_true',help='Print every account requiring this Sunday review.')
    mode.add_argument('--state',action='store_true',help='Print recent weekly-run results.')
    mode.add_argument('--input',help='Save a complete weekly refresh JSON payload.')
    args=parser.parse_args()
    init_db()
    if args.eligible:
        show_eligible()
    elif args.state:
        show_state()
    else:
        save_input(args.input)


if __name__ == '__main__':
    try:
        main()
    except ValueError as exc:
        print(json.dumps({'ok':False,'error':str(exc)}),file=sys.stderr)
        sys.exit(2)
