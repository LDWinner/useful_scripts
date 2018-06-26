#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os
import fnmatch
import re

def traverse():
    re_h = re.compile(r'.*\.(h|hpp)$')
    linesInFile = []
    with open("/home/wei/.vim/.ycm_extra_conf.py","r") as ycm:
        for line in ycm:
            linesInFile.append(line)
    for root,dir,files in os.walk("."):
        for file in files:
            if re_h.match(file):
                linesInFile.insert(86,"'-isystem',\n")
                linesInFile.insert(87,"'" + root + "',\n")
                break
    s = ''.join(linesInFile)
    with open("./.ycm_extra_conf.py","w") as f:
        f.write(s)


if __name__ == '__main__':
    traverse()


