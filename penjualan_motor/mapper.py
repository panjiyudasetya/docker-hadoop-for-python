#!/usr/bin/env python

"""
A Python code to Map the input data.

It prints out the input data that comes from the Python STDIN
(standard input) as a pair of Key/Value.

- The `Key` refers to the trivial word, and
- The `Value` refers to the count of that trivial word.
"""

import sys

# Get all input that comes from the Python STDIN (standard input)
input_lines = sys.stdin

# Converts every line in the input lines as a pair of Key/Value
for line in input_lines:
    # Removes leading and trailing whitespace
    line = line.strip()

    # Splits the line into words
    words = line.split()

    # Increase counters
    for word in words:
        # Write the results through the Python STDOUT (standard output);
        # What we output here, we will use it as the input for the Reduce step,
        # i.e. the input for reducer.py
        #
        # We use tab-delimiter to separate the pair of key and value;
        # The trivial word count is 1
        print('%s\t%s' % (word, 1))
