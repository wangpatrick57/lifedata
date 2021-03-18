import unittest
import os
import shutil
from helpers import *
from lifelog import *
from datetime import *

TESTING_HOME_DIR = f'{REPO_HOME_DIR}/logging/testing_home'
LATEST_LOG_FNAME = f'{TESTING_HOME_DIR}/latest_log.txt'
SUMMARY_FNAME = f'{TESTING_HOME_DIR}/summary.csv'

class Tests(unittest.TestCase):
    def setUp(self):
        assert not os.path.isdir(TESTING_HOME_DIR), 'please remove the already existent testing directory'

        try:
            os.makedirs(TESTING_HOME_DIR)
        except:
            cls.tearDownClass()
            raise

    def tearDown(self):
        shutil.rmtree(TESTING_HOME_DIR)

    def test_date_helpers(self):
        dt1 = datetime(2020, 1, 2, 5, 38)
        dt2 = datetime(2020, 1, 2, 8, 22)
        self.assertTrue(is_same_day(dt1, dt2))
        self.assertFalse(is_next_day(dt1, dt2))
        self.assertFalse(is_next_day(dt2, dt1))
        self.assertEqual(calculate_activity_minutes(dt1, dt2), 164)

        dt1 = datetime(2020, 1, 2, 5, 38)
        dt2 = datetime(2020, 1, 3, 8, 22)
        self.assertFalse(is_same_day(dt1, dt2))
        self.assertTrue(is_next_day(dt1, dt2))
        self.assertFalse(is_next_day(dt2, dt1))
        self.assertEqual(calculate_activity_minutes(dt1, dt2), 1440 + 164)

        dt1 = datetime(2020, 2, 29, 5, 38)
        dt2 = datetime(2020, 3, 1, 8, 22)
        self.assertFalse(is_same_day(dt1, dt2))
        self.assertTrue(is_next_day(dt1, dt2))
        self.assertFalse(is_next_day(dt2, dt1))
        self.assertEqual(calculate_activity_minutes(dt1, dt2), 1440 + 164)

        dt1 = datetime(2020, 12, 31, 5, 38)
        dt2 = datetime(2021, 1, 1, 8, 22)
        self.assertFalse(is_same_day(dt1, dt2))
        self.assertTrue(is_next_day(dt1, dt2))
        self.assertFalse(is_next_day(dt2, dt1))
        self.assertEqual(calculate_activity_minutes(dt1, dt2), 1440 + 164)

        dt1 = datetime(2020, 12, 31, 5, 38)
        dt2 = datetime(2021, 5, 5, 8, 22)
        self.assertFalse(is_same_day(dt1, dt2))
        self.assertFalse(is_next_day(dt1, dt2))
        self.assertFalse(is_next_day(dt2, dt1))
        self.assertEqual(calculate_activity_minutes(dt1, dt2), 381)

    def test_basic_logging(self):
        self.assertFalse(os.path.isfile(LATEST_LOG_FNAME))

        # first log
        log_activity(datetime(2020, 1, 2, 5, 37), 'FUNN', TESTING_HOME_DIR, True)
        data_fname = f'{TESTING_HOME_DIR}/data/2020/1/2020_01_02.txt'
        self.assertTrue(os.path.isfile(LATEST_LOG_FNAME))
        self.assertTrue(os.path.isfile(data_fname))
        self.file_assert_lines(LATEST_LOG_FNAME, ['2020-01-02 FUNN 05_37'])
        self.file_assert_lines(data_fname, ['UNKN 00_00', 'FUNN 05_37'])

        # same day
        log_activity(datetime(2020, 1, 2, 18, 5), 'YTBE', TESTING_HOME_DIR, True)
        self.file_assert_lines(LATEST_LOG_FNAME, ['2020-01-02 YTBE 18_05'])
        self.file_assert_lines(data_fname, ['UNKN 00_00', 'FUNN 05_37', 'YTBE 18_05'])

        # new day, same month, same year
        log_activity(datetime(2020, 1, 12, 3, 20), 'DEEP', TESTING_HOME_DIR, True)
        data_fname = f'{TESTING_HOME_DIR}/data/2020/1/2020_01_12.txt'
        self.assertTrue(os.path.isfile(data_fname))
        self.file_assert_lines(LATEST_LOG_FNAME, ['2020-01-12 DEEP 03_20'])
        self.file_assert_lines(data_fname, ['YTBE 00_00', 'DEEP 03_20'])

        # new day, different month, same year
        log_activity(datetime(2020, 11, 3, 7, 18), 'SHAL', TESTING_HOME_DIR, True)
        data_fname = f'{TESTING_HOME_DIR}/data/2020/11/2020_11_03.txt'
        self.assertTrue(os.path.isfile(data_fname))
        self.file_assert_lines(LATEST_LOG_FNAME, ['2020-11-03 SHAL 07_18'])
        self.file_assert_lines(data_fname, ['DEEP 00_00', 'SHAL 07_18'])

        # new day, different month, different year
        log_activity(datetime(2021, 2, 10, 0, 3), 'WOUT', TESTING_HOME_DIR, True)
        data_fname = f'{TESTING_HOME_DIR}/data/2021/2/2021_02_10.txt'
        self.assertTrue(os.path.isfile(data_fname))
        self.file_assert_lines(LATEST_LOG_FNAME, ['2021-02-10 WOUT 00_03'])
        self.file_assert_lines(data_fname, ['SHAL 00_00', 'WOUT 00_03'])

    def test_summary(self):
        self.assertFalse(os.path.isfile(LATEST_LOG_FNAME))

        # first activity
        log_activity(datetime(2020, 1, 2, 5, 37), 'FUNN', TESTING_HOME_DIR, True)
        self.assertFalse(os.path.isfile(SUMMARY_FNAME))
        assert_lines = []

        # first log
        log_activity(datetime(2020, 1, 2, 6, 50), 'YTBE', TESTING_HOME_DIR, True)
        self.assertTrue(os.path.isfile(SUMMARY_FNAME))
        assert_lines.append('date,funn_time')
        assert_lines.append('2020-01-02,73')
        self.file_assert_lines(SUMMARY_FNAME, assert_lines)

        # new day but no log
        log_activity(datetime(2020, 1, 3, 1, 22), 'SHAL', TESTING_HOME_DIR, True)
        self.file_assert_lines(SUMMARY_FNAME, assert_lines)

        # two funn activities in a day
        log_activity(datetime(2020, 1, 3, 2, 30), 'FUNN', TESTING_HOME_DIR, True)
        self.file_assert_lines(SUMMARY_FNAME, assert_lines)
        log_activity(datetime(2020, 1, 3, 3, 35), 'SHAL', TESTING_HOME_DIR, True)
        assert_lines.append('2020-01-03,65')
        self.file_assert_lines(SUMMARY_FNAME, assert_lines)
        log_activity(datetime(2020, 1, 3, 3, 40), 'FUNN', TESTING_HOME_DIR, True)
        self.file_assert_lines(SUMMARY_FNAME, assert_lines)
        log_activity(datetime(2020, 1, 3, 3, 50), 'SHAL', TESTING_HOME_DIR, True)
        assert_lines[-1] = '2020-01-03,75'
        self.file_assert_lines(SUMMARY_FNAME, assert_lines)

        # adding across one day
        log_activity(datetime(2020, 1, 5, 2, 30), 'FUNN', TESTING_HOME_DIR, True)
        self.file_assert_lines(SUMMARY_FNAME, assert_lines)
        log_activity(datetime(2020, 1, 6, 19, 23), 'SHAL', TESTING_HOME_DIR, True)
        assert_lines.append('2020-01-05,2453')
        self.file_assert_lines(SUMMARY_FNAME, assert_lines)

        # not adding, when it's across multiple days
        log_activity(datetime(2020, 1, 8, 2, 30), 'FUNN', TESTING_HOME_DIR, True)
        self.file_assert_lines(SUMMARY_FNAME, assert_lines)
        log_activity(datetime(2020, 1, 10, 19, 23), 'SHAL', TESTING_HOME_DIR, True)
        assert_lines.append('2020-01-08,569')
        self.file_assert_lines(SUMMARY_FNAME, assert_lines)

        # exact same time
        log_activity(datetime(2020, 1, 12, 2, 23, 0), 'FUNN', TESTING_HOME_DIR, True)
        self.file_assert_lines(SUMMARY_FNAME, assert_lines)
        log_activity(datetime(2020, 1, 12, 2, 23, 59), 'SHAL', TESTING_HOME_DIR, True)
        assert_lines.append('2020-01-12,0')
        self.file_assert_lines(SUMMARY_FNAME, assert_lines)

    def file_assert_lines(self, fname, assert_lines):
        f = open(fname, 'r')
        file_array = [line.strip() for line in f]
        file_array_str = '\n'.join(file_array)
        self.assertTrue(len(file_array) == len(assert_lines), f'the file {fname} has {len(file_array)} lines while assert_array has {len(assert_lines)}. here is what the file looks like:\n{file_array_str}')

        for file_line, assert_line in zip(file_array, assert_lines):
            self.assertTrue(file_line == assert_line, f'the line "{assert_line}" is not in the file {fname}. here is what the file looks like:\n{file_array_str}')

        f.close()

if __name__ == '__main__':
    unittest.main()
