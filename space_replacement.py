#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os


path = sys.argv[1]
replacement = sys.argv[2]
files = os.listdir(path)


for file in files:
    old = os.path.join(path, file)
    new = replacement.join(old.split())

    os.rename(old, new)
