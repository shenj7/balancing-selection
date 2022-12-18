from argparse import ArgumentParser
import datetime
import os
import random
#from ..script_generator.generate_eidos_script import generate_eidos_script
import sys
#from ..summary_statistic_calculator.summary_statistic_dataframe_generator import create_statistics_csv
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
                        help="Eidos script directory")
    parser.add_argument('-n',
                        '--number_of_scripts',
                        required=True,
                        help="Number of scripts to generate")
    parser.add_argument('-s',
                        '--seed',
                        default='0',
                        help="Random seed for Eidos script")
    parser.add_argument('-cl',
                        '--minimum-selection_coefficient',
                        required=True,
                        help="minimum selection coefficient",
                        type=int)
    parser.add_argument('-cr',
                        '--maximum-selection_coefficient',
                        required=True,
                        help="maximum selection coefficient",
                        type=int)
    parser.add_argument('-ml',
                        '--minimum_mutation_rate',
                        required=True,
                        help="Minimum population mutation rate",
                        type=int)
    parser.add_argument('-mr',
                        '--maximum_mutation_rate',
                        required=True,
                        help="Maximum population mutation rate",
                        type=int)
    parser.add_argument('-rl',
                        '--minimum_recombination_rate',
                        required=True,
                        help="Minimum recombination rate",
                        type=int)
    parser.add_argument('-rr',
                        '--maximum_recombination_rate',
                        required=True,
                        help="Maximum recombination rate",
                        type=int)
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
    parser.add_argument('-sz',
                        '--size',
                        default='10',
                        help="Window size of windows",
                        type=int)
    parser.add_argument('-sd',
                        '--stats_directory',
                        required=True,
                        help="Output directory for stats csv")
    parser.add_argument('-ps',
                        '--path_to_slim',
                        default='/work/williarj/2223balancing_selection/slimexe',
                        help="Path to slim executable")

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
    print(os.getcwd())
    args = command_line_parser(main_args)
    # file output for results from simulations will be in args.directory/<guid>
    # quick thought: is a guid ok, or should we make smth more descriptive such as seed.mutation_rate.~~
    os.system(f"mkdir {args.directory}")
    os.system(f"mkdir {args.directory}/outputs")
    random.seed(args.seed)
    vcf_files = []
    filenames = []
    for _ in range(int(args.number_of_scripts)):
        seed = random.randint(0, 100000)
        mutation_rate = random.uniform(args.minimum_mutation_rate,
                                       args.maximum_mutation_rate)
        recombination_rate = random.uniform(args.minimum_recombination_rate,
                                            args.maximum_recombination_rate)
        population_size = random.randint(args.minimum_population_size,
                                         args.maximum_population_size)
        selection_coefficient = random.randint(args.minimum_selection_coefficient,
                                         args.maximum_selection_coefficient)
        filename = f"{seed}_{mutation_rate}_{recombination_rate}_{population_size}_{datetime.datetime.now()}"  # TODO
        filenames.append(filename)
        output_location = f"{args.directory}/{filename}.vcf"
        vcf_files.append(output_location)
        generate_eidos_script(filename, seed, mutation_rate,
                              recombination_rate, selection_coefficient, population_size,
                              output_location)
        os.system(f"{args.path_to_slim} {filename}")

    for k in range(len(filenames)):     
        stats_output_location = f"{args.stats_directory}/{filenames[k]}.csv" 
        create_statistics_csv(vcf_files[k], args.size, stats_output_location)

if __name__ == '__main__':
    main(sys.argv[1:])
