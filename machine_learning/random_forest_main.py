import sys
from machine_learning_model_generator import create_machine_learning_model
from sklearn.ensemble import RandomForestClassifier as rf
from machine_learning_command_line_parser import command_line_parser

def main(main_args=None):
    args = command_line_parser(main_args)

    forest = rf()
    create_machine_learning_model(args.directory, forest, './generated_forests/forest1.pkl')


if __name__ == '__main__':
    main(sys.argv[1:])
