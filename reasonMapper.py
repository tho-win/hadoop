#!/usr/bin/env python3

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    carrierDelay = ""
    weatherDelay = ""
    NASDelay = ""
    securityDelay = ""
    lateAircraftDelay = ""
    curIndex = 0
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(",")
    # increase counters
    for word in words:
        if curIndex == 58: carrierDelay = word
        if curIndex == 59: weatherDelay = word
        if curIndex == 60: NASDelay = word
        if curIndex == 61: securityDelay = word
        if curIndex == 62: lateAircraftDelay = word
        curIndex = curIndex + 1
    #print(airline)
    #print(depDel15)
    #print(arrDel15)
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    #
    # tab-delimited; the trivial word count is 1
    if carrierDelay != "1.00" and carrierDelay != "":
        print("{0}\t1".format("Carrier delay"))
    if weatherDelay != "1.00" and weatherDelay != "":
        print("{0}\t1".format("Weather delay"))
    if NASDelay != "1.00" and NASDelay != "":
        print("{0}\t1".format("NAS delay"))
    if securityDelay != "1.00" and securityDelay != "":
        print("{0}\t1".format("Security delay"))
    if lateAircraftDelay != "1.00" and lateAircraftDelay != "":
        print("{0}\t1".format("Late aircraft"))
