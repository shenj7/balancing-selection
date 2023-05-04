from pgmpy.models.BayesianNetwork import BayesianNetwork
import sys
from machine_learning_model_generator import create_machine_learning_model
from machine_learning_model_generator import create_machine_learning_model_discretized
from machine_learning_model_generator import create_frame
from machine_learning_command_line_parser import command_line_parser
from pgmpy.inference.ExactInference import VariableElimination
import numpy as np
import joblib
from bayesian_network_model import MyBayesianModel


def create_bayesian_network(dir):
    df = create_frame(dir)

    bs_model = BayesianNetwork([('Pi', 'tajima_d'), ('watterson_theta', 'tajima_d'),
                              ('h1', 'h12'), ('h1', 'h123'), ('h1', 'h2_h1'), ('h12', 'h123'), ('h12', 'h2_h1'),
                              ('tajima_d', 'bsb'), ('h123', 'bsb'), ('h2_h1', 'bsb')])

    bs_model = MyBayesianModel(bs_model)

    return bs_model


def main(main_args=None):
    args = command_line_parser(main_args)

    bn = create_bayesian_network(args.directory)

    create_machine_learning_model_discretized(args.directory, bn, './generated_bayesian_networks/bn1.pkl', './generated_bayesian_networks/bn1.csv', './generated_bayesian_networks/bn1_roc.png', './generated_bayesian_networks/bins/', 11)

    joblib.dump(bn.bs_model, './generated_bayesian_networks/bn1.pkl')

    # randomized_grid_search()


if __name__ == '__main__':
    main(sys.argv[1:])
