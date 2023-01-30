import numpy as np
import pandas as pd
from pathlib import Path as pt
from sklearn.naive_bayes import GaussianNB as bnb
from sklearn.model_selection import train_test_split
import joblib


def create_frame(dir):
    files = pt(dir).glob("*")
    summary = None
    created = False
    for file in files:
        df = pd.read_csv(file)
        if not created:
            summary=df
            created = True
        else:
            summary = summary.append(df, ignore_index=True)
    return summary.dropna()


def create_train_and_test_data(features, target, seed):
    if seed == None:
        print('No seed given for splitting train and test data')
    features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=seed)
    return features_train, features_test, target_train, target_test


def find_TP(true, pred):
    # counts the number of true positives (y_true = 1, y_pred = 1)
    return sum((true == 1) & (pred == 1))


def find_FN(true, pred):
    # counts the number of false negatives (y_true = 1, y_pred = 0)
    return sum((true == 1) & (pred == 0))


def find_FP(true, pred):
    # counts the number of false positives (y_true = 0, y_pred = 1)
    return sum((true == 0) & (pred == 1))


def find_TN(true, pred):
    # counts the number of true negatives (y_true = 0, y_pred = 0)
    return sum((true == 0) & (pred == 0))


def calculate_accuracy(forest, features_test, target_test):
    pred_test = forest.predict(features_test)
    accuracy = (find_TP(target_test, pred_test) + find_TN(target_test, pred_test))/(find_TP(target_test, pred_test) + find_TN(target_test, pred_test) + find_FP(target_test, pred_test) + find_FN(target_test, pred_test))
    return accuracy


def calculate_precision(forest, features_test, target_test):
    pred_test = forest.predict(features_test)
    precision = find_TP(target_test, pred_test)/(find_TP(target_test, pred_test) + find_FP(target_test, pred_test))
    return precision


def calculate_recall(forest, features_test, target_test):
    pred_test = forest.predict(features_test)
    recall = find_TP(target_test, pred_test)/(find_TP(target_test, pred_test) + find_FN(target_test, pred_test))
    return recall


def calculate_f1(forest, features_test, target_test):
    f1 = (2 * (calculate_precision(forest, features_test, target_test) * calculate_recall(forest, features_test, target_test)))/(calculate_precision(forest, features_test, target_test) + calculate_recall(forest, features_test, target_test))
    return f1

# def plot_roc_curve(forest, features_test, target_test):
#     plot_roc_curve(forest, features_test, target_test)


def create_naive_bayes(dir):
    df = create_frame(dir)

    features = df.drop(['bs', 'bsb', 'left_window', 'right_window'], axis=1)
    target = df['bsb']

    features_train, features_test, target_train, target_test = create_train_and_test_data(features, target, 1)

    nb = bnb()
    nb.fit(features_train, target_train)

    print('Accuracy:', calculate_accuracy(nb, features_test, target_test))
    print('Precision:', calculate_precision(nb, features_test, target_test))
    print('Recall:', calculate_recall(nb, features_test, target_test))
    print('F1:', calculate_f1(nb, features_test, target_test))

    # plot_roc_curve(forest, features_test, target_test)

    joblib.dump(nb, './generated_naive_bayes/nb1.pkl')

    return nb