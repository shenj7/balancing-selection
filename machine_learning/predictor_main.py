from argparse import ArgumentParser
import joblib
from machine_learning_predictor import model_predict
import sys

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
    args = parser.parse_args(main_args)
    return args

def main(main_args=None):
    args = command_line_parser(main_args)
    dir = args.directory
    model_location = args.model
    bins = args.bins

    model = joblib.load(model_location)
    
    model_predict(model, dir, bins)


if __name__ == '__main__':
    main(sys.argv[1:])