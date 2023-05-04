import pandas as pd
from argparse import ArgumentParser
import sys

def command_line_parser(main_args):
    parser = ArgumentParser(description="filter predictions")
    parser.add_argument('-f',
                        '--filename',
                        required=True,
                        help="The prediction file")
    args = parser.parse_args(main_args)
    return args

def main(main_args=None):
    args = command_line_parser(main_args)
    filename = args.filename
    df = pd.read_csv(filename)
    df.query("pred == 1").drop(['Pi', 'watterson_theta', 'tajima_d', 'h1', 'h12', 'h123', 'h2_h1', 'bs', 'bsb'], axis=1).to_csv(filename[0:len(filename)-4] + '_filtered.csv')

if __name__ == '__main__':
    main(sys.argv[1:])
