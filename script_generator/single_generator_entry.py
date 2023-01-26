from argparse import ArgumentParser
import sys

from generate_eidos_script import generate_eidos_script
"""
Entry point for generating a single Eidos script
Note: This entry point is mainly for testing specific scripts,
    see multiple_generator_entry.py for the main entry point
"""


def command_line_parser(main_args):
    parser = ArgumentParser(description="Generates eidos scripts")
    parser.add_argument('-f',
                        '--filename',
                        required=True,
                        help="Output location for Eidos script")
    parser.add_argument('-s',
                        '--seed',
                        default='0',
                        help="Random seed for Eidos script")
    parser.add_argument('-c',
                        '--selection_coefficient',
                        default='0.001',
                        help="Selection coefficient")
    parser.add_argument('-d',
                        '--dominance_coefficient',
                        required=True,
                        help="dominance coefficient",
                        type=float)
    parser.add_argument('-m',
                        '--mutation_rate',
                        required=True,
                        help="Population mutation rate")
    parser.add_argument('-r',
                        '--recombination_rate',
                        required=True,
                        help="Population mutation rate")
    parser.add_argument('-ll',
                        '--left_limit',
                        required=True,
                        help="Left limit for balancing selection locus",
                        type=int)
    parser.add_argument('-lr',
                        '--right_limit',
                        required=True,
                        help="Right limit for balancing selection locus",
                        type=int)
    parser.add_argument('-p',
                        '--population_size',
                        required=True,
                        help="Population size")
    parser.add_argument('-g',
                        '--genome_size',
                        required=True,
                        help="genome size",
                        type=int)
    parser.add_argument('-o',
                        '--output_location',
                        required=True,
                        help="Output location for run data")

    args = parser.parse_args(main_args)
    return args


def main(main_args=None):
    args = command_line_parser(main_args)
    generate_eidos_script(args.filename, args.seed, args.mutation_rate,
                          args.recombination_rate, args.selection_coefficient, args.dominance_coefficient,
                          args.left_limit, args.right_limit,
                          args.population_size, args.output_location)


if __name__ == '__main__':
    main(sys.argv[1:])