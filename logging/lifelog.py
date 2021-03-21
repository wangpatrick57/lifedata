import sys
from datetime import *
from helpers import *

REPO_HOME_DIR = '/Users/patrickwang/Documents/inUse/lifedata'
SUMMARY_FNAME = f'{REPO_HOME_DIR}/summary.csv'
USAGE_MSG = f'USAGE: python3 lifelog.py activityName [time]\n\tvalid activityNames: {VALID_ACTIVITIES_STR}'

def main() -> None:
    if len(sys.argv) < 2:
        print(USAGE_MSG)
        return

    if sys.argv[1].lower() == 'summary':
        print(''.join(open(SUMMARY_FNAME, 'r').readlines()), end='')
        return
    elif sys.argv[1].lower() == 'today':
        today_data_fname = get_data_fname(datetime.now(), REPO_HOME_DIR)
        print(''.join(open(today_data_fname, 'r').readlines()), end='')
        return
    elif sys.argv[1].lower() == 'paths':
        today_data_fname = get_data_fname(datetime.now(), REPO_HOME_DIR)
        print(f'Today\'s data: {today_data_fname}')
        print(f'Summary file: {SUMMARY_FNAME}')
        return

    activity = sys.argv[1].upper()
    dt = datetime.now()

    if len(sys.argv) == 3:
        input_hour, input_minute = [int(data) for data in sys.argv[2].split('_')]
        dt = datetime(dt.year, dt.month, dt.day, input_hour, input_minute)

    log_activity(dt, activity, REPO_HOME_DIR)

if __name__ == '__main__':
    main()
