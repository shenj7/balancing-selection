import pandas as pd
from pathlib import Path as pt
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
            summary = pd.concat([summary, df], ignore_index=True)
    summary = summary.drop(['Unnamed: 0'], axis=1)
    print(summary.shape)
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


def calculate_accuracy(model, pred_test, target_test):
    accuracy = (find_TP(target_test, pred_test) + find_TN(target_test, pred_test))/(find_TP(target_test, pred_test) + find_TN(target_test, pred_test) + find_FP(target_test, pred_test) + find_FN(target_test, pred_test))
    return accuracy


def calculate_precision(model, pred_test, target_test):
    precision = find_TP(target_test, pred_test)/(find_TP(target_test, pred_test) + find_FP(target_test, pred_test))
    return precision


def calculate_recall(model, pred_test, target_test):
    recall = find_TP(target_test, pred_test)/(find_TP(target_test, pred_test) + find_FN(target_test, pred_test))
    return recall


def calculate_f1(model, pred_test, target_test):
    f1 = (2 * (calculate_precision(model, pred_test, target_test) * calculate_recall(model, pred_test, target_test))) / (calculate_precision(model, pred_test, target_test) + calculate_recall(model, pred_test, target_test))
    return f1


def create_test_output(model, features_test, target_test, pred_test, test_output):
    features_test['bsb_true'] = target_test
    features_test['bsb_predicted'] = pred_test

    features_test.to_csv(test_output)


def create_machine_learning_model(dir, model, output_name, test_output):
    df = create_frame(dir)
    print(df.shape)
    features = df.drop(['bs', 'bsb', 'left_window', 'right_window'], axis=1)
    target = df['bsb']
    bin_data(features)
    features_train, features_test, target_train, target_test = create_train_and_test_data(features, target, 1)

    model.fit(features_train, target_train)

    pred_test = model.predict(features_test)

    print('Accuracy:', calculate_accuracy(model, pred_test, target_test))
    print('Precision:', calculate_precision(model, pred_test, target_test))
    print('Recall:', calculate_recall(model, pred_test, target_test))
    print('F1:', calculate_f1(model, pred_test, target_test))

    create_test_output(model, features_test, target_test, pred_test, test_output)

    joblib.dump(model, output_name)


def bin_data(features):
    pi, pi_bins = pd.qcut(features['Pi'], 7, retbins=True, labels=False)
    features['Pi'] = pi
    watterson_theta, watterson_theta_bins = pd.qcut(features['watterson_theta'], 7, retbins=True, labels=False)
    features['watterson_theta'] = watterson_theta
    tajima_d, tajima_d_bins = pd.qcut(features['tajima_d'], 7, retbins=True, labels=False)
    features['tajima_d'] = tajima_d
    h1, h1_bins = pd.qcut(features['h1'], 7, retbins=True, labels=False)
    features['h1'] = h1
    h12, h12_bins = pd.qcut(features['h12'], 7, retbins=True, labels=False)
    features['h12'] = h12
    h123, h123_bins = pd.qcut(features['h123'], 7, retbins=True, labels=False)
    features['h123'] = h123
    h2_h1, h2_h1_bins = pd.qcut(features['h2_h1'], 7, retbins=True, labels=False)
    features['h2_h1'] = h2_h1
    return features, pi_bins, watterson_theta_bins, tajima_d_bins, h1_bins, h12_bins, h123_bins, h2_h1_bins


def create_machine_learning_model_discretized(dir, model, output_name, test_output):
    df = create_frame(dir)
    features = df.drop(['bs', 'bsb', 'left_window', 'right_window'], axis=1)

    binned, pi_bins, watterson_theta_bins, tajima_d_bins, h1_bins, h12_bins, h123_bins, h2_h1_bins = bin_data(features)
    features = binned

    target = df['bsb']

    print(target.shape)

    features_train, features_test, target_train, target_test = create_train_and_test_data(features, target, 1)

    model.fit(features_train, target_train)

    pred_test = model.predict(features_test)

    print('Accuracy:', calculate_accuracy(model, pred_test, target_test))
    print('Precision:', calculate_precision(model, pred_test, target_test))
    print('Recall:', calculate_recall(model, pred_test, target_test))
    print('F1:', calculate_f1(model, pred_test, target_test))

    create_test_output(model, features_test, target_test, pred_test, test_output)

    joblib.dump(model, output_name)
