#!/usr/bin/env python

import argparse
import sys
from . import Diary


def main():
    parser = argparse.ArgumentParser(description="Create markdown diary file templates.")
    parser.add_argument("when", help="Generate a diary file for the given month or year. e.g. 2018 or 2018-12",
                        type=str)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    month = Diary.Diary.valid_month(args.when)
    year = Diary.Diary.valid_year(args.when)
    if month:
        Diary.Diary.create_month_file(month)
    elif year:
        Diary.Diary.create_year_files(year)
    else:
        print("Error: The value " + args.when + " is not a valid year/month combination")
        parser.print_help(sys.stderr)
        sys.exit(1)
