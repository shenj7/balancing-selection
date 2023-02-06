import sys
from machine_learning_model_generator import create_machine_learning_model
from sklearn.ensemble import RandomForestClassifier as rf
from machine_learning_command_line_parser import command_line_parser
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def calculate_forest_feature_importance(forest):
    feature_names = ['Pi', 'watterson_theta', 'tajima_d', 'h1', 'h12', 'h123', 'h2_h1']
    importances = forest.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
    forest_importances = pd.Series(importances, index=feature_names)
    fig, ax = plt.subplots()
    forest_importances.plot.bar(yerr=std, ax=ax)
    ax.set_title("Feature importances using MDI")
    ax.set_ylabel("Mean decrease in impurity")
    fig.tight_layout()
    plt.show()


def main(main_args=None):
    args = command_line_parser(main_args)

    forest = rf()

    create_machine_learning_model(args.directory, forest, './generated_forests/forest1.pkl', './generated_forests/forest1.csv')
    calculate_forest_feature_importance(forest)

if __name__ == '__main__':
    main(sys.argv[1:])
