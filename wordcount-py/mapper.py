#!/usr/bin/env python

"""
A Python code to Map the input data.

It prints out the input data that comes from the Python STDIN
(standard input) as a pair of Key/Value.

- The `Key` refers to the trivial word, and
- The `Value` refers to the count of that trivial word.
"""

import sys

class Mapper:
    word_count_dict = dict()

    def map(self):
        # Get all input that comes from the Python STDIN (standard input)
        input_lines = sys.stdin

        self._count_words_in_lines(input_lines)
        self._print_result()

    def _count_words_in_lines(self, lines):

        for line in lines:
            # Removes leading and trailing whitespace
            cleaned_line = line.strip()

            self._count_words_in_line(cleaned_line)

    def _count_words_in_line(self, line):

        # Splits the line into words
        words = line.split()

        # Increase counters
        for word in words:
            if self.word_count_dict.get(word):
                self.word_count_dict[word] += 1
            else:
                self.word_count_dict[word] = 1

    def _print_result(self):
        """
        Write the results through the Python STDOUT (standard output);
        What we output here, we will use it as the input for the Reduce step.
        i.e. the input for the `reducer.py`

        We use tab-delimiter to separate the pair of key and value;
        """

        for word, counter in self.word_count_dict.items():
            print('%s\t%s' % (word, counter))


if __name__ == '__main__':
    Mapper().map()
