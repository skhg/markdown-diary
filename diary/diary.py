#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from datetime import datetime, timedelta
import calendar
import os

parser = argparse.ArgumentParser()
parser.add_argument("month", help="month to generate a diary page for. e.g. 2018-12",
                    type=str)
args = parser.parse_args()

try:
    month = datetime.strptime(args.month, '%Y-%m')
except ValueError:
    print('Error: \'' + args.month + '\' is not a valid YYYY-MM year/month combination')
    exit()

filename = str(month.strftime('%m')) + ' ' + str(month.strftime('%B')) + '.md'

if os.path.exists(filename):
    print('Error: Diary \'' + filename + '\' already exists')
    exit(1)

days_in_month = calendar.monthrange(month.year, month.month)[1]

with open(filename, 'w') as open_file:
    open_file.writelines('# ' + month.strftime('%B') + '\n')
    open_file.writelines('\n')

    current_week = 0

    for d in range(0, days_in_month):
        todays_date = month + timedelta(days=d)

        temp_week = int(todays_date.strftime('%W')) + 1

        if current_week != temp_week:
            current_week = temp_week
            open_file.writelines('\n')
            open_file.writelines('\n')
            open_file.writelines('## Week ' + str(current_week) + '\n')
            open_file.writelines('\n')

        day_of_week = int(todays_date.strftime('%w'))

        if day_of_week != 0 and day_of_week != 6:
            open_file.writelines('### ' + todays_date.strftime('%a') + ' ' + todays_date.strftime('%-d') + '\n')
            open_file.writelines('\n')
            open_file.writelines('\n')
