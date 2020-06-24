#!/usr/bin/env python

from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='markdown-diary',
    version='0.0.0',
    description="CLI tool to generate monthly diary files in simple Markdown format",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='diary journal markdown cli',
    author='Jack Higgins',
    author_email='pypi@jackhiggins.ie',
    url='https://github.com/skhg/markdown-diary',
    packages=['py_markdown_diary'],
    entry_points={
        'console_scripts': ['md-diary=py_markdown_diary.command_line:main'],
    },
    install_requires=[
    ],
    tests_require=[
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'])
