import math
from argparse import ArgumentParser
import datetime
import os
import random
import sys
import threading

from script_generator import generate_eidos_script
from summary_statistic_calculator import create_statistics_csv_from_file

# importlib.import_module('script_generator.generate_eidos_script', '.')
# importlib.import_module('summary_statistic_calculator.dataframe_generator', '.')

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
                        nargs="+",
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
                        required=True,
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
                        nargs="+",
                        help="minimum dominance coefficient",
                        type=float)
    parser.add_argument('-dr',
                        '--maximum_dominance_coefficient',
                        required=True,
                        nargs="+",
                        help="maximum dominance coefficient",
                        type=float)
    parser.add_argument('-lll',
                        '--minimum_left_limit',
                        required=True,
                        nargs="+",
                        help="Left limit for balancing selection locus",
                        type=int)
    parser.add_argument('-llr',
                        '--maximum_left_limit',
                        required=True,
                        nargs="+",
                        help="Left limit for balancing selection locus",
                        type=int)
    parser.add_argument('-lrl',
                        '--minimum_right_limit',
                        required=True,
                        nargs="+",
                        help="Right limit for balancing selection locus",
                        type=int)
    parser.add_argument('-lrr',
                        '--maximum_right_limit',
                        required=True,
                        nargs="+",
                        help="Right limit for balancing selection locus",
                        type=int)

    parser.add_argument('-gr',
                        '--maximum_genome_size',
                        required=True,
                        nargs="+",
                        help="Maximum genome size",
                        type=int)
    parser.add_argument('-gl',
                        '--minimum_genome_size',
                        required=True,
                        nargs="+",
                        help="Maximum genome size",
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
                        default='/work/williarj/2223_balancing_selection/slimexe',
                        help="Path to slim executable")

    args = parser.parse_args(main_args)
    return args


def slim_thread(pts, filename):
    os.system(f"{pts} {filename}")


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
    os.system(f"mkdir big_scripts/{args.stats_directory}")
    random.seed(args.seed)
    for i, directory in enumerate(args.directory):
        filenames = []
        vcf_files = []
        bs_ranges = []
        os.system(f"mkdir big_scripts/{directory}")
        os.system(f"mkdir big_scripts/{directory}/outputs")
        for _ in range(args.number_of_scripts[i]):
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
            left_limit = random.randint(args.minimum_left_limit[i],
                                        args.maximum_left_limit[i])
            right_limit = random.randint(args.minimum_right_limit[i],
                                         args.maximum_right_limit[i])
            genome_size = random.randint(args.minimum_genome_size[i],
                                         args.maximum_genome_size[i])
            seed = random.randint(0, 0xffffffff)
            filename = f"{seed}_{mutation_rate}_{recombination_rate}_{population_size}_{datetime.date.today()}"  # TODO
            filenames.append(filename)
            bs_ranges.append([left_limit, right_limit])
            output_location = f"big_scripts/{directory}/outputs/{filename}.vcf"
            filename = f"big_scripts/{directory}/{filename}"
            vcf_files.append(output_location)
            generate_eidos_script(filename, seed, mutation_rate,
                                  recombination_rate, selection_coefficient, dominance_coefficient,
                                  left_limit, right_limit,
                                  population_size, genome_size, output_location)

        threads = []

        for filename in filenames:
            fn = f"big_scripts/{directory}/{filename}"
            thread = threading.Thread(target=slim_thread, args=(args.path_to_slim, fn))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        for k in range(len(filenames)):
            stats_output_location = f"big_scripts/{args.stats_directory}/{filenames[k]}.csv"
            create_statistics_csv_from_file(vcf_files[k], args.size, stats_output_location, bs_ranges[k][0], bs_ranges[k][1])


if __name__ == '__main__':
    main(sys.argv[1:])
