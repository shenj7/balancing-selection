from argparse import ArgumentParser
import datetime
import os
import random
import sys
import importlib
importlib.import_module('script_generator.generate_eidos_script', '.')
importlib.import_module('summary_statistic_calculator.dataframe_generator', '.')

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
                        nargs=
                        help="Eidos script directory")
    parser.add_argument('-n',
                        '--number_of_scripts',
                        required=True,
                        nargs="+",
                        help="Number of scripts to generate",
                        type=int)
    parser.add_argument('-s',
                        '--seed',
                        default='0',
                        nargs="+",
                        help="Random seed for Eidos script")
    parser.add_argument('-cl',
                        '--minimum-selection_coefficient',
                        required=True,
                        nargs="+",
                        help="minimum selection coefficient",
                        type=float)
    parser.add_argument('-cr',
                        '--maximum-selection_coefficient',
                        required=True,
                        nargs="+",
                        help="maximum selection coefficient",
                        type=float)
    parser.add_argument('-ml',
                        '--minimum_mutation_rate',
                        required=True
                        nargs="+",
                        help="Minimum population mutation rate",
                        type=float)
    parser.add_argument('-mr',
                        '--maximum_mutation_rate',
                        required=True,
                        nargs="+",
                        help="Maximum population mutation rate",
                        type=float)
    parser.add_argument('-rl',
                        '--minimum_recombination_rate',
                        required=True,
                        nargs="+",
                        help="Minimum recombination rate",
                        type=float)
    parser.add_argument('-rr',
                        '--maximum_recombination_rate',
                        required=True,
                        nargs="+",
                        help="Maximum recombination rate",
                        type=float)
    parser.add_argument('-pl',
                        '--minimum_population_size',
                        required=True,
                        nargs="+",
                        help="Minimum population size",
                        type=int)
    parser.add_argument('-pr',
                        '--maximum_population_size',
                        required=True,
                        nargs="+",
                        help="Maximum population size",
                        type=int)
    parser.add_argument('-dl',
                        '--minimum_dominance_coefficient',
                        required=True,
                        help="minimum dominance coefficient",
                        type=float)
    parser.add_argument('-dr',
                        '--maximum_dominance_coefficient',
                        required=True,
                        help="maximum dominance coefficient",
                        type=float)
    parser.add_argument('-sz',
                        '--size',
                        default='10',
                        nargs="+",
                        help="Window size of windows",
                        type=int)
    parser.add_argument('-sd',
                        '--stats_directory',
                        required=True,
                        nargs="+",
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
    args = command_line_parser(main_args)
    # file output for results from simulations will be in args.directory/<guid>
    # quick thought: is a guid ok, or should we make smth more descriptive such as seed.mutation_rate.~~
    os.system(f"mkdir big_scripts")

    for i, seed in enumerate(args.seed):
        random.seed(args.seed)
        for _ in range(args.number_of_scripts[i]):
            os.system(f"mkdir big_scripts/{args.directory[i]}")
            os.system(f"mkdir big_scripts/{args.directory[i]}/outputs")
            mutation_rate = random.uniform(args.minimum_mutation_rate[i],
                                           args.maximum_mutation_rate[i])
            recombination_rate = random.uniform(args.minimum_recombination_rate[i],
                                                args.maximum_recombination_rate[i])
            population_size = random.randint(args.minimum_population_size[i],
                                             args.maximum_population_size[i])
            selection_coefficient = random.uniform(args.minimum_selection_coefficient[i],
                                                   args.maximum_selection_coefficient[i])
            dominance_coefficient = random.uniform(args.minimum_dominance_coefficient[i],
                                                   args.maximum_dominance_coefficient[i])
            filename = f"big_scripts/{args.directory[i]}/{seed}_{mutation_rate}_{recombination_rate}_{population_size}_{datetime.datetime.now()}"  # TODO
            output_location = f"big_scripts/{args.directory[i]}/outputs/{filename}.vcf"
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
