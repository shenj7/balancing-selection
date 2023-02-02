from argparse import ArgumentParser


def command_line_parser(main_args):
    parser = ArgumentParser(description="Trains the random forest")
    parser.add_argument('-d',
                        '--directory',
                        required=True,
                        help="the summary statistic files of the random forest")
    args = parser.parse_args(main_args)
    return args
