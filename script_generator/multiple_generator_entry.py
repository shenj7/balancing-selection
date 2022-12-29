import os
import random
import datetime
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
    parser.add_argument('-d',
                        '--directory',
                        required=True,
                        help="Output directory for Eidos scripts")
    parser.add_argument('-cl',
                        '--minimum-selection_coefficient',
                        required=True,
                        help="minimum selection coefficient",
                        type=float)
    parser.add_argument('-cr',
                        '--maximum-selection_coefficient',
                        required=True,
                        help="maximum selection coefficient",
                        type=float)
    parser.add_argument('-n',
                        '--number_of_scripts',
                        required=True,
                        help="Number of scripts to generate",
                        type=int)
    parser.add_argument('-s',
                        '--seed',
                        default='0',
                        help="Random seed for Eidos script",
                        type=int)
    parser.add_argument('-ml',
                        '--minimum_mutation_rate',
                        required=True,
                        help="Minimum population mutation rate",
                        type=float)
    parser.add_argument('-mr',
                        '--maximum_mutation_rate',
                        required=True,
                        help="Maximum population mutation rate",
                        type=float)
    parser.add_argument('-rl',
                        '--minimum_recombination_rate',
                        required=True,
                        help="Minimum recombination rate",
                        type=float)
    parser.add_argument('-rr',
                        '--maximum_recombination_rate',
                        required=True,
                        help="Maximum recombination rate",
                        type=float)
    parser.add_argument('-pl',
                        '--minimum_population_size',
                        required=True,
                        help="Minimum population size",
                        type=int)
    parser.add_argument('-pr',
                        '--maximum_population_size',
                        required=True,
                        help="Maximum population size",
                        type=int)

    args = parser.parse_args(main_args)
    return args


def main(main_args=None):
    """
    Generates a folder with multiple runs with the following structure:
    scripts/
    ├─ output/
    │  ├─ script_1-output.vcf
    │  ├─ script_2-output.vcf
    ├─ script_1
    ├─ script_2

    """
    args = command_line_parser(main_args)
    # file output for results from simulations will be in args.directory/<guid>
    # quick thought: is a guid ok, or should we make smth more descriptive such as seed.mutation_rate.~~
    os.system(f"mkdir {args.directory}")
    os.system(f"mkdir {args.directory}/outputs")
    random.seed(args.seed)
    for _ in range(args.number_of_scripts):
        seed = random.randint(0, 10000000)
        mutation_rate = random.uniform(args.minimum_mutation_rate,
                                       args.maximum_mutation_rate)
        recombination_rate = random.uniform(args.minimum_recombination_rate,
                                            args.maximum_recombination_rate)
        population_size = random.randint(args.minimum_population_size,
                                         args.maximum_population_size)
        selection_coefficient = random.uniform(args.minimum_selection_coefficient,
                                         args.maximum_selection_coefficient)
        filename = f"{seed}_{mutation_rate}_{recombination_rate}_{population_size}_{datetime.datetime.now()}"  # TODO
        output_location = f"{args.directory}/{filename}.vcf"
        generate_eidos_script(filename, seed, mutation_rate,
                              recombination_rate, selection_coefficient, population_size,
                              output_location)


if __name__ == '__main__':
    main(sys.argv[1:])
