import os
from single_generator_entry import generate_eidos_script

from argparse import ArgumentParser
import sys

from generate_eidos_script import generate_eidos_script

"""
Entry point for generating multiple Eidos scripts
Note: This is the main entry point for this script,
    allowing multiple Eidos scripts to be generated using
    the input parameters
"""

def command_line_parser(main_args):
    parser = ArgumentParser(description="Generates eidos scripts")
    parser.add_argument('-d', '--directory', required=True,
        help="Output directory for Eidos scripts")
    parser.add_argument('-n', '--number_of_scripts', required=True,
        help="Number of scripts to generate")
    parser.add_argument('-ml', '--minimum_mutation_rate', required=True,
        help="Minimum population mutation rate")
    parser.add_argument('-mr', '--maximum_mutation_rate', required=True,
        help="Maximum population mutation rate")
    parser.add_argument('-rl', '--minimum_recombination_rate', required=True,
        help="Minimum recombination rate")
    parser.add_argument('-rr', '--maximum_recombination_rate', required=True,
        help="Maximum recombination rate")
    parser.add_argument('-pl', '--minimum_population_size', required=True,
        help="Minimum population size")
    parser.add_argument('-pr', '--maximum_population_size', required=True,
        help="Maximum population size")

    args = parser.parse_args(main_args)
    return args

def main(main_args=None):
    args = command_line_parser(main_args)
    # file output for results from simulations will be in args.directory/<guid>
    # quick thought: is a guid ok, or should we make smth more descriptive such as seed.mutation_rate.~~
    os.system(f"mkdir ")
    for _ in range(args.number_of_scripts):
        generate_eidos_script()

if __name__ == '__main__':
    main(sys.argv[1:])