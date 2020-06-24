# markdown-diary

[![Build Status](https://travis-ci.org/skhg/diary.svg?branch=master)](https://travis-ci.org/skhg/diary)

Diary file template generator, producing text files in [Markdown](https://en.wikipedia.org/wiki/Markdown) format.

I use this personally to keep a simple monthly diary of my notes and activities. Since it just produces a series of text files, they can be stored in something like Dropbox, and synced everywhere easily. 

## Installation
`pip install markdown-diary`

## How to use

Generate a diary file for a month, in the current directory:

Run `md-diary -m YYYY-MM` (e.g. `md-diary -m 2019-01`) which will create a file called `01 January.md`

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

* python 2 or 3
