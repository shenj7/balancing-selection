import os
import random
import datetime

from argparse import ArgumentParser
import sys

"""
Entry point for running a directory with a bunch of script subirectories
"""


def command_line_parser(main_args):
    parser = ArgumentParser(description="Generates eidos scripts")
    parser.add_argument('-d',
                        '--directory',
                        required=True,
                        help="relative path to directory containing directories of scripts generated")
    args = parser.parse_args(main_args)
    return args


def main(main_args=None):
    """
    Starts runs, 
    """
    args = command_line_parser(main_args)
    directory = args.directory
    run_dirs = next(os.walk(f"./{directory}"))[1]
    for dir in run_dirs:
        os.system("cp run_scripts_parallel.bash ./{directory}/{dir}/run.bash")
        os.system("./{directory}/{dir}/run.bash")
        with open("run_tracker", "a") as f:
            f.write(f"{dir}")
        

if __name__ == '__main__':
    main(sys.argv[1:])
