#!/usr/bin/env python3

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    worstAirlines = ["\"DL\"", "\"AA\"", "\"WN\""]
    airline = ""
    destCity = ""
    destState = ""
    depDel15 = ""
    arrDel15 = ""
    curIndex = 0
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(",")
    # increase counters
    for word in words:
        if curIndex == 6: airline = word
        elif curIndex == 25: destCity = word
        elif curIndex == 26: destState = word
        elif curIndex == 35: depDel15 = word
        elif curIndex == 46: arrDel15 = word
        curIndex = curIndex + 1
    #print(airline)
    #print(depDel15)
    #print(arrDel15)
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    #
    # tab-delimited; the trivial word count is 1
    if depDel15 == "1.00" and arrDel15 == "1.00" and airline in worstAirlines:
        print("{0}, {1}\t1".format(destCity, destState))
