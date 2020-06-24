#!/usr/bin/env python

import argparse
import sys
from . import Diary


def main():
    parser = argparse.ArgumentParser(description="Create markdown diary file templates.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-m", "--month", help="Generate a diary file for the given month. e.g. 2018-12",
                       type=str)
    group.add_argument("-y", "--year", help="Generate a set of diary files for the given year. e.g. 2020",
                       type=str)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    if args.year:
        valid_year = Diary.Diary.validate_year(args.year)
        Diary.Diary.create_year_files(valid_year)
    elif args.month:
        valid_month = Diary.Diary.validate_month(args.month)
        Diary.Diary.create_month_file(valid_month)
