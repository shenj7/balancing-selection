import sys
from machine_learning_model_generator import create_machine_learning_model
from sklearn.ensemble import RandomForestClassifier as rf
from machine_learning_command_line_parser import command_line_parser
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def calculate_forest_feature_importance(forest):
    feature_names = ['\u03C0', '\u03B8_w', 'D', 'H1', 'H12', 'H123', 'H2\H1']
    importances = forest.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
    forest_importances = pd.Series(importances, index=feature_names)
    fig, ax = plt.subplots(figsize=(3.2, 4.8))
    forest_importances.plot.barh(yerr=std, ax=ax)
    ax.set_title("Feature importances using MDI", fontdict={'size': 24})
    ax.set_xlabel("Mean decrease in impurity", fontdict={'size': 20})
    fig.tight_layout()
    #plt.show()
    plt.savefig('feature_importance.png')


def main(main_args=None):
    args = command_line_parser(main_args)

    forest = rf()

    create_machine_learning_model(args.directory, forest, './generated_forests/forest1.pkl', './generated_forests/forest1.csv')
    calculate_forest_feature_importance(forest)

if __name__ == '__main__':
    main(sys.argv[1:])
