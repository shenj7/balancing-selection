from argparse import ArgumentParser
import sys
import os
from naive_bayes_generator import create_naive_bayes


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
    nb_classifier = create_naive_bayes(args.directory)


if __name__ == '__main__':
    main(sys.argv[1:])
