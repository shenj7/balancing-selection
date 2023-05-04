from argparse import ArgumentParser
import joblib
from machine_learning_predictor import model_predict
import sys
import pandas as pd
from bayesian_network_model import MyBayesianModel

def command_line_parser(main_args):
    parser = ArgumentParser(description="Trains the random forest")
    parser.add_argument('-d',
                        '--directory',
                        required=True,
                        help="the summary statistic files")
    parser.add_argument('-m',
                        '--model',
                        required=True,
                        help="The model used for prediction")
    parser.add_argument('-b',
                        '--bins',
                        help="If using model trained on bins, the bins")
    parser.add_argument('-p',
                        '--prediction_location',
                        help="Where the prediction goes",
                        required=True,)
    parser.add_argument('-bn',
                        '--is_bayesian_network',
                        help="is a bayesian network")
    args = parser.parse_args(main_args)
    return args

def main(main_args=None):
    args = command_line_parser(main_args)
    dir = args.directory
    model_location = args.model
    bins = args.bins
    prediction_location = args.prediction_location
    is_bayesian_network = args.is_bayesian_network

    model = joblib.load(model_location)
    if (is_bayesian_network != None):
        model = MyBayesianModel(model)

    model_predict(model, dir, bins, prediction_location)

if __name__ == '__main__':
    main(sys.argv[1:])
