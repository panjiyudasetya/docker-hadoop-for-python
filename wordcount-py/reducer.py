#!/usr/bin/env python

"""
A Python code to Reduce the list of the datasets of key/value.

It prints out the dataset of Key/Value pairs that we got from the `mapper.py`.
And then we will aggregates the dataset based on their Key.

- The `Key` refers to the trivial word, and
- The `Value` refers to the count of that trivial word.
"""

import sys


class Reducer:
    word_count_dict = dict()

    def reduce(self):
        self._reduce_word_counter()
        self._print_result()

    def _reduce_word_counter(self):

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

            if self.word_count_dict.get(word):
                self.word_count_dict[word] += count
            else:
                self.word_count_dict[word] = count

    def _print_result(self):

        for word, counter in self.word_count_dict.items():
            print('%s\t%s' % (word, counter))


if __name__ == '__main__':
    Reducer().reduce()
