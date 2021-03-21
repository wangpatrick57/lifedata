from datetime import *
import os
import re

VALID_ACTIVITY_NAMES = {'SLLP', 'BIOL', 'WOUT', 'SOCL', 'SHAL', 'DEEP', 'YTBE', 'FUNN', 'UNKN'}
VALID_ACTIVITIES_STR = ', '.join(VALID_ACTIVITY_NAMES)

DATE_OPTION = 0
TIME_OPTION = 1

# returns (YYYY, MM, DD, HH, MM)
def extract_from_dt(dt: datetime) -> (str, str, str, str, str):
    return (dt.year, dt.month, dt.day, dt.hour, dt.minute)

def dt_to_str(dt: datetime, option: int, sep: str) -> str:
    if option == DATE_OPTION:
        return f'{dt.year}{sep}{str(dt.month).zfill(2)}{sep}{str(dt.day).zfill(2)}'
    elif option == TIME_OPTION:
        return f'{str(dt.hour).zfill(2)}{sep}{str(dt.minute).zfill(2)}'

def strs_to_dt(date_str: str, time_str: str) -> datetime:
    year, month, day = [int(data) for data in re.split('[^0-9]', date_str)]
    hour, minute = [int(data) for data in re.split('[^0-9]', time_str)]
    return datetime(year, month, day, hour, minute)

def get_data_fname(dt: datetime, home_dir: str) -> str:
    year, month, day, hours, minutes = extract_from_dt(dt)
    return f'{home_dir}/data/{year}/{month}/{dt_to_str(dt, DATE_OPTION, "_")}.txt'

def log_activity(dt: datetime, activity: str, home_dir: str, for_testing=False) -> bool:
    # check if valid activity name otherwise
    if activity not in VALID_ACTIVITY_NAMES:
        if not for_testing:
            print(USAGE_MSG)

        return

    # create latest_log.txt if necessary
    latest_log_fname = f'{home_dir}/latest_log.txt'

    if not os.path.isfile(latest_log_fname):
        f = open(latest_log_fname, 'w')
        f.write(f'0001-01-01 UNKN 00_00')
        f.close()

    # read from latest_log.txt
    f = open(latest_log_fname, 'r')
    latest_log_date_str, latest_log_activity, latest_log_time_str = f.read().strip().split(' ')
    latest_log_dt = strs_to_dt(latest_log_date_str, latest_log_time_str)
    f.close()

    # create directory if necessary
    data_fname = get_data_fname(dt, home_dir)

    if not os.path.exists(os.path.dirname(data_fname)):
        try:
            os.makedirs(os.path.dirname(data_fname))
        except OSError as err:
            if err.errno != errno.EEXIST:
                raise

    # create data file if necessary, using latest_log_activity
    if not os.path.isfile(data_fname):
        f = open(data_fname, 'w')
        f.write(f'{latest_log_activity} 00_00\n')
        f.close()

    # add to data file
    f = open(data_fname, 'a')
    data = f'{activity} {dt_to_str(dt, TIME_OPTION, "_")}\n'
    f.write(data)
    f.close()

    # update summary file
    if latest_log_activity == 'FUNN':
        write_to_summary_file(latest_log_dt, calculate_activity_minutes(latest_log_dt, dt), activity, home_dir)

    # update latest_log file
    f = open(latest_log_fname, 'w')
    f.write(f'{dt_to_str(dt, DATE_OPTION, "-")} {activity} {dt_to_str(dt, TIME_OPTION, "_")}')
    f.close()

    if not for_testing:
        print(f'Logged {activity} {dt_to_str(dt, TIME_OPTION, "_")} to {data_fname}')

def crop_seconds(dt: datetime) -> datetime:
    return datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)

def calculate_activity_minutes(start_dt: datetime, end_dt: datetime) -> int:
    if is_same_day(start_dt, end_dt) or is_next_day(start_dt, end_dt):
        end_to_to_use = end_dt
    else:
        end_to_to_use = get_end_of_day(start_dt)

    return round((crop_seconds(end_to_to_use) - crop_seconds(start_dt)).total_seconds() / 60)

def is_same_day(start_dt: datetime, end_dt: datetime) -> bool:
    return start_dt.year == end_dt.year and start_dt.month == end_dt.month and start_dt.day == end_dt.day

def is_next_day(start_dt: datetime, end_dt: datetime) -> bool:
    start_next_day_dt = start_dt + timedelta(days=1)
    return is_same_day(start_next_day_dt, end_dt)

def get_end_of_day(dt: datetime):
    return datetime(dt.year, dt.month, dt.day, 11, 59)

def write_to_summary_file(dt: datetime, minutes_to_add: int, activity: str, home_dir: str) -> None:
    summary_fname = f'{home_dir}/summary.csv'
    summary_dict = dict()

    if os.path.isfile(summary_fname):
        with open(summary_fname, 'r') as f:

            for line in f.readlines()[1:]:
                date_str, funn_time_str = line.strip().split(',')
                summary_dict[date_str] = int(funn_time_str)

    curr_date_str = dt_to_str(dt, DATE_OPTION, '-')

    if curr_date_str not in summary_dict:
        summary_dict[curr_date_str] = 0

    summary_dict[curr_date_str] += minutes_to_add

    with open(summary_fname, 'w') as f:
        f.write('date,funn_time\n')

        for date in sorted(summary_dict.keys()):
            f.write(f'{date},{summary_dict[date]}\n')
