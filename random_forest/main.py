from argparse import ArgumentParser
import sys
import os
from random_forest_generator import create_random_forest


def command_line_parser(main_args):
    parser = ArgumentParser(description="Trains the random forest")
    parser.add_argument('-d',
                        '--directory',
                        required=True,
                        help="the summary statistic files of the random forest")
    args = parser.parse_args(main_args)
    return args


def main(main_args=None):
    args = command_line_parser(main_args)
    forest_classifier = create_random_forest(args.directory)


if __name__ == '__main__':
    main(sys.argv[1:])
