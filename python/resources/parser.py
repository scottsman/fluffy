"""Parser that will read in a txt file with multiple ascii art and create a txt file for each.
Left aligns and removes blank lines from above and below.

Assumptions:
    * In source txt file, each ascii art is separated by at least one blank line.

TODO:
    * Be able to pull located the artist signature from the art, remove it, and add it
        to the next txt file in a standarized way to be read by fluffy.
"""
import argparse
import random
import string


def parse_args():
    parser = argparse.ArgumentParser(
        description="Parse a txt file with ascii art."
    )
    parser.add_argument('file_path',
        help="The txt file to parse."
    )
    return parser.parse_args()


def main(file_path):
    # A list of lists.
    ascii_objects = []

    # Read the txt and extract each art into an ascii_object.
    with open(file_path, 'r') as fd:
        ascii_object = []
        for line in fd:
            if line.isspace():
                if ascii_object:
                    ascii_objects.append(ascii_object)
                ascii_object = []
            else:
                ascii_object.append(line)

    # For the ascii_objects, left align.
    for ascii_object in ascii_objects:
        # Fine the smallest amount of whitespace.
        min_whitespace = None
        for line in ascii_object:
            whitespace = len(line) - len(line.lstrip())
            if min_whitespace is None or whitespace < min_whitespace:
                min_whitespace = whitespace

        for count, line in enumerate(ascii_object):
            ascii_object[count] = line[min_whitespace:]

    # Write out art in separate random files.
    for ascii_object in ascii_objects:
        random_name = ''.join([random.choice(string.ascii_letters) for _ in range(6)])
        file_name = "%s.txt" % random_name
        with open(file_name, 'w') as fd:
            fd.writelines(ascii_object)

if __name__ == '__main__':
    args = parse_args()
    main(args.file_path)

