#!/usr/bin/env python
# Syntax: duplicates.py DIRECTORY

import os
import sys

top = sys.argv[1]
d = {}

file_count = 0

BLACKLIST = [".DS_Store", ]

for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        file_count += 1
        fn = os.path.join(root, name)
        basename, extension = os.path.splitext(name)

        # Enable this if you want to ignore case.
        # basename = basename.lower()

        if basename not in BLACKLIST:
            sys.stdout.write(
                "Scanning... %s files scanned.  Currently looking at ...%s/\r" %
                 (file_count, root[-50:])
            )

            if basename in d:
                d[basename].append(fn)
            else:
                d[basename] = [fn, ]

print("\nDone scanning. Here are the duplicates found: ")

for k, v in d.items():
    if len(v) > 1:
        print("%s (%s):" % (k, len(v)))
        for f in v:
            print (f)
