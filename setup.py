#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import codecs
import os
import sys
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

if __name__ == "__main__":
    setup(
        name = 'keep',
        packages = ['keep', 'keep.commands'],
        version = "1.3.1",
        description = 'Personal shell command keeper',
        long_description = long_description,
        author = 'Himanshu Mishra',
        author_email = 'himanshumishra@iitkgp.ac.in',
        url = "https://github.com/orkohunter/keep",
        download_url = "https://github.com/orkohunter/keep/archive/master.zip",
        include_package_data=True,
        install_requires=[
            'click',
            'requests',
            'tabulate'
        ],
        entry_points = {
            'console_scripts': [
                'keep = keep.cli:cli'
            ],
        },
    )

