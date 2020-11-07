import sys
import datetime
import os
from helpers import *

def main() -> None:
    if len(sys.argv) < 2:
        print(USAGE_MSG)
        return

    activity = sys.argv[1]

    if activity not in VALID_ACTIVITY_NAMES:
        print(USAGE_MSG)
        return

    dt = datetime.datetime.now()
    year, month, day, hours, minutes = format_datetime(dt)
    data_fname = f'../data/{year}/{month}/{year}_{month}_{day}.txt'

    # create directory if necessary
    if not os.path.exists(os.path.dirname(data_fname)):
        try:
            os.makedirs(os.path.dirname(data_fname))
        except OSError as err:
            if err.errno != errno.EEXIST:
                raise

    # create prevActivityName.txt if necessary
    if not os.path.isfile(PREV_ACTIVITY_FNAME):
        f = open(PREV_ACTIVITY_FNAME, 'w')
        f.write(f'UNKN')
        f.close()

    f = open(PREV_ACTIVITY_FNAME, 'r')
    prevActivityName = f.read()
    f.close()

    # create file with prevActivityName if necessary
    if not os.path.isfile(data_fname):
        f = open(data_fname, 'w')
        f.write(f'{prevActivityName} 00_00\n')
        f.close()

    # write activity
    f = open(data_fname, 'a')
    data = f'{activity} {hours}_{minutes}\n'
    f.write(data)
    f.close()
    print(f'Wrote {data.strip()} to {data_fname}')
    f = open(PREV_ACTIVITY_FNAME, 'w')
    f.write(f'{activity}')
    f.close()
    print(f'Wrote {activity} to {PREV_ACTIVITY_FNAME}')

if __name__ == '__main__':
    main()
