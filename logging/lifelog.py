import sys
from datetime import *
from helpers import *

REPO_HOME_DIR = '/Users/patrickwang/Documents/inUse/lifedata'
USAGE_MSG = f'USAGE: python3 lifelog.py activityName [time]\n\tvalid activityNames: {VALID_ACTIVITIES_STR}'

def main() -> None:
    if len(sys.argv) < 2:
        print(USAGE_MSG)
        return

    activity = sys.argv[1].upper()
    dt = datetime.now()

    if len(sys.argv) == 3:
        input_hour, input_minute = [int(data) for data in sys.argv[2].split('_')]
        dt = datetime(dt.year, dt.month, dt.day, input_hour, input_minute)

    log_activity(dt, activity, REPO_HOME_DIR)

if __name__ == '__main__':
    main()
