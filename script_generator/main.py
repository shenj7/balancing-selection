from argparse import ArgumentParser
import sys

from generate_eidos_script import generate_eidos_script

def command_line_parser(main_args):
    parser = ArgumentParser(description="Generates eidos scripts")
    parser.add_argument('-f', '--filename', required=True,
        help="Output location for Eidos script")
    parser.add_argument('-s', '--seed', default='0',
        help="Random seed for Eidos script")
    parser.add_argument('-m', '--mutation_rate', required=True,
        help="Population mutation rate")
    parser.add_argument('-r', '--recombination_rate', required=True,
        help="Population mutation rate")
    parser.add_argument('-p', '--population_size', required=True,
        help="Population size")
    parser.add_argument('-o', '--output_location', required=True,
        help="Output location for run data")

    args = parser.parse_args(main_args)
    return args

def main(main_args=None):
    args = command_line_parser(main_args)
    generate_eidos_script(args.filename, args.seed, args.mutation_rate, args.recombination_rate, args.population_size, args.output_location)

if __name__ == '__main__':
    main(sys.argv[1:])