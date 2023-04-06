import sys
from machine_learning_model_generator import create_machine_learning_model
from sklearn.naive_bayes import GaussianNB as bnb
from machine_learning_command_line_parser import command_line_parser


def main(main_args=None):
    args = command_line_parser(main_args)
    nb_classifier = bnb()
    create_machine_learning_model(args.directory, nb_classifier, './generated_naive_bayes/nb1.pkl', './generated_naive_bayes/nb1.csv', './generated_naive_bayes/nb1_roc.png')


if __name__ == '__main__':
    main(sys.argv[1:])
