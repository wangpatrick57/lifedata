import datetime

VALID_ACTIVITY_NAMES = {'SLLP', 'BIOL', 'WOUT', 'SOCL', 'SHAL', 'DEEP', 'YTBE', 'FUNN', 'UNKN'}
VALID_ACTIVITIES_STR = ', '.join(VALID_ACTIVITY_NAMES)
PREV_ACTIVITY_FNAME = '../prevActivityName.txt'
USAGE_MSG = f'USAGE: python3 lifelog.py [activityName]\n\tvalid activityNames: {VALID_ACTIVITIES_STR}'

# returns (YYYY, MM, DD, HH, MM)
def format_datetime(dt: datetime.datetime) -> (str, str, str, str, str):
    dtstr = str(dt)
    datestr, timestr = dtstr.split(' ')
    year, month, day = datestr.split('-')
    hours, minutes, _ = timestr.split(':')
    return (year, month, day, hours, minutes)
