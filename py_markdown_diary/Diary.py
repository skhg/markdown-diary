from datetime import datetime, date, timedelta
import calendar
import os


class Diary(object):

    @staticmethod
    def valid_month(month_str):
        try:
            return datetime.strptime(month_str, '%Y-%m')
        except ValueError:
            return None

    @staticmethod
    def valid_year(year_str):
        try:
            return datetime.strptime(year_str, '%Y')
        except ValueError:
            return None

    @staticmethod
    def write_month_file(month, filename, weekdays_only):
        days_in_month = calendar.monthrange(month.year, month.month)[1]

        with open(filename, 'w') as open_file:
            open_file.writelines('# ' + month.strftime('%B') + '\n')
            open_file.writelines('\n')

            current_week = 0

            for d in range(0, days_in_month):
                today_date = month + timedelta(days=d)

                temp_week = int(today_date.strftime('%W')) + 1

                if current_week != temp_week:
                    current_week = temp_week
                    open_file.writelines('\n')
                    open_file.writelines('\n')
                    open_file.writelines('## Week ' + str(current_week) + '\n')
                    open_file.writelines('\n')

                day_of_week = int(today_date.strftime('%w'))

                is_weekend = day_of_week == 0 or day_of_week == 6

                if not is_weekend or (is_weekend and not weekdays_only):
                    open_file.writelines('### ' + today_date.strftime('%a') + ' ' + today_date.strftime('%-d') + '\n')
                    open_file.writelines('\n')
                    open_file.writelines('\n')

    @staticmethod
    def create_month_file(month, weekdays_only):
        filename = str(month.strftime('%m')) + ' ' + str(month.strftime('%B')) + '.md'

        if not Diary.file_exists(filename):
            Diary.write_month_file(month, filename, weekdays_only)

    @staticmethod
    def create_year_files(year, weekdays_only):
        for m in range(1, 13):
            Diary.create_month_file(date(year.year, m, 1), weekdays_only)

    @staticmethod
    def file_exists(filename):
        if os.path.exists(filename):
            print('Note: Diary \'' + filename + '\' already exists. Will not be modified.')
            return True

        return False
