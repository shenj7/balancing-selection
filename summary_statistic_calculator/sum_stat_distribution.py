from argparse import ArgumentParser
import sys
import matplotlib.pyplot as plt
from pathlib import Path as pt
import pandas as pd

def command_line_parser(main_args):
    parser = ArgumentParser(description="Creates a histogram of summary statistics")
    parser.add_argument('-d',
                        '--directory',
                        required=True,
                        help="the directory of the summary statistics")
    parser.add_argument('-o',
                        '--output',
                        required=True,
                        help="the output of the histograms")

    args = parser.parse_args(main_args)
    return args


def create_frame(dir):
        files = pt(dir).glob("*")
        summary = None
        created = False
        for file in files:
            df = pd.read_csv(file)
            if not created:
                summary=df
                created = True
            else:
                summary = pd.concat([summary, df], ignore_index=True)
        summary = summary.drop(['Unnamed: 0'], axis=1)
        return summary.dropna()


def create_histograms(directory, output):
    df = create_frame(directory)
    plt.hist(df['Pi'], 4)
    plt.savefig(output + '/pi_dist.png')
    plt.clf()

    plt.hist(df['watterson_theta'], 4)
    plt.savefig(output + '/watterson_theta_dist.png')
    plt.clf()

    plt.hist(df['tajima_d'], 4)
    plt.savefig(output + '/tajima_d_dist.png')
    plt.clf()

    plt.hist(df['h1'], 4)
    plt.savefig(output + '/h1_dist.png')
    plt.clf()

    plt.hist(df['h12'], 4)
    plt.savefig(output + '/h12_dist.png')
    plt.clf()

    plt.hist(df['h123'], 4)
    plt.savefig(output + '/h123_dist.png')
    plt.clf()

    plt.hist(df['h2_h1'], 4)
    plt.savefig(output + '/h2_h1_dist.png')
    plt.clf()

def main(main_args=None):
    args = command_line_parser(main_args)
    directory = args.directory
    output = args.output

    create_histograms(directory, output)


if __name__ == '__main__':
    main(sys.argv[1:])
