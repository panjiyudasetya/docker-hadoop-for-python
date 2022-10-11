#!/usr/bin/env python

"""
A Python code to Reduce the list of the datasets of key/value.

It prints out the dataset of Key/Value pairs that we got from the `mapper.py`.
And then we will aggregates the dataset based on their Key.

- The `Key` refers to the trivial word, and
- The `Value` refers to the count of that trivial word.
"""

import sys

current_word = None
current_count = 0
word = None

# An input comes from the Python STDIN (standard input)
for line in sys.stdin:
    # Removes leading and trailing whitespace
    line = line.strip()

    # Parse the input we got from the `mapper.py`
    word, count = line.split('\t', 1)

    # Convert count (currently a string) to an integer
    try:
        count = int(count)
    except ValueError:
        # Count was not a number, so silently
        # ignore/discard this line
        continue

    # The IF-switch only works because Hadoop sorts the Map output by key (here: word)
    # before it is passed to the Reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print ('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# Do not forget to output the last word if needed!
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
