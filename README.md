# diary

[![Build Status](https://travis-ci.org/skhg/diary.svg?branch=master)](https://travis-ci.org/skhg/diary)

Markdown diary file generator

## How to run

`python diary.py YYYY-MM`

e.g. `python diary.py 2019-01`

This produces a markdown file named `01 January.md` in the current directory, formatted for daily diary entries, with day and week numbers.

The format looks like:

```
# January



## Week 1

### Tue 1


### Wed 2


### Thu 3


### Fri 4




## Week 2

### Mon 7


### Tue 8
```
## Dependencies

* python 3