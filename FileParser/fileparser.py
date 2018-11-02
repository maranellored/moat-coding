#!/usr/bin/env python

################################################################################
##
##  Fileparser script.
##  Helps parse a file to count the following
##  - Blank lines
##  - Tabs
##  - Open Braces
##  - Closed braces
##  - Open brackets
##  - Closed Brackets
##  - newlines
##
################################################################################

import sys


def usage():
    print "Usage:\n{} <path/to/file>".format(sys.argv[0])
    sys.exit(1)


def run():
    # Make sure that we have atleast 1 argument passed in
    # on the cmd line.
    if len(sys.argv) != 2:
        usage()

    # assumes that the path is the absolute path to the file.
    file = sys.argv[1]
    with open(file) as f:
        content = f.readlines()

    # The number of new line characters is the number of lines in the file.
    new_lines = len(content)
    tabs = 0
    open_braces = 0
    closed_braces = 0
    open_brackets = 0
    closed_brackets = 0
    blank_lines = 0

    for line in content:
        # Count each of the required characters.
        open_braces += line.count('{')
        closed_braces += line.count('}')
        open_brackets += line.count('(')
        closed_brackets += line.count(')')
        tabs += line.count('\t')

        # A blank line is one that has only the new line character.
        # The length of the line is 1.
        if len(line) == 1:
            # Found a blank line!
            blank_lines += 1

    print "Number of open braces - {}".format(open_braces)
    print "Number of closed braces - {}".format(closed_braces)
    print "Number of open brackets - {}".format(open_brackets)
    print "Number of closed brackets - {}".format(closed_brackets)
    print "Number of blank lines - {}".format(blank_lines)
    print "Number of new lines - {}".format(new_lines)
    print "Number of tabs - {}".format(tabs)

if __name__ == '__main__':
    run()
