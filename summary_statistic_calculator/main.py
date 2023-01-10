from argparse import ArgumentParser
from dataframe_generator import create_statistics_csv_from_file
from dataframe_generator import create_statistics_csv_from_directory
import sys

def command_line_parser(main_args):
    parser = ArgumentParser(description="Calculates summary statistics")
    parser.add_argument('-f',
                        '--filename',
                        help="Location of vcf file",)
    parser.add_argument('-d',
                        '--directory',
                        help="directory of vcf files")
    parser.add_argument('-s',
                        '--size',
                        default='10',
                        help="Window size of windows",
                        type=int)
    parser.add_argument('-o',
                        '--output',
                        required=True,
                        help="Output location for summary statistics")
    parser.add_argument('-bl',
                        '--balancing-left',
                        required=True,
                        help="starting point of balancing selection area",
                        type=int)
    parser.add_argument('-br',
                        '--balancing-right',
                        required=True,
                        help="ending point of balancing selection area",
                        type=int)

    args = parser.parse_args(main_args)
    return args

def main(main_args=None):
    args = command_line_parser(main_args)
    if args.filename == None:
        create_statistics_csv_from_directory(args.directory, args.size, args.output, args.balancing_left, args.balancing_right)
    else:
        create_statistics_csv_from_file(args.filename, args.size, args.output, args.balancing_left, args.balancing_right)

if __name__ == '__main__':
    main(sys.argv[1:])