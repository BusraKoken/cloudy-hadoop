#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import string

def read_input(file):
    for line in file:
        yield [word.strip(string.punctuation) for word in line.split()]


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            print '%s%s%d' % (word, separator, 1)

if __name__ == "__main__":
    main()