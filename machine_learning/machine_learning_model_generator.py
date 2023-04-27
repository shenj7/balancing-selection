import pandas as pd
from pathlib import Path as pt
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
import joblib
import matplotlib.pyplot as plt


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


def plot_roc_curve(pred_test, target_test, roc_output):
    fpr, tpr, thresholds = roc_curve(target_test, pred_test)
    fig, ax = plt.subplots()
    plt.plot(fpr, tpr)
    ax.set_title("ROC Curve", fontdict={'size': 24})
    ax.set_xlabel("False Positive Rate", fontdict={'size': 20})
    ax.set_ylabel("True Positive Rate", fontdict={'size': 20})
    fig.tight_layout()
    # plt.show()
    plt.savefig(roc_output)


def create_machine_learning_model(dir, model, output_name, test_output, roc_output):
    df = create_frame(dir)
    print(df.shape)
    features = df.drop(['bs', 'bsb', 'left_window', 'right_window'], axis=1)
    target = df['bsb']
    features_train, features_test, target_train, target_test = create_train_and_test_data(features, target, 1)

    model.fit(features_train, target_train)

    pred_test = model.predict(features_test)

    print('Accuracy:', calculate_accuracy(model, pred_test, target_test))
    print('Precision:', calculate_precision(model, pred_test, target_test))
    print('Recall:', calculate_recall(model, pred_test, target_test))
    print('F1:', calculate_f1(model, pred_test, target_test))

    plot_roc_curve(pred_test, target_test, roc_output)

    create_test_output(model, features_test, target_test, pred_test, test_output)

    joblib.dump(model, output_name)


def bin_data(features, num_bins):
    pi, pi_bins = pd.qcut(features['Pi'], num_bins, retbins=True, labels=False, duplicates='drop')
    features['Pi'] = pi
    watterson_theta, watterson_theta_bins = pd.qcut(features['watterson_theta'], num_bins, retbins=True, labels=False, duplicates='drop')
    features['watterson_theta'] = watterson_theta
    tajima_d, tajima_d_bins = pd.qcut(features['tajima_d'], num_bins, retbins=True, labels=False, duplicates='drop')
    features['tajima_d'] = tajima_d
    h1, h1_bins = pd.qcut(features['h1'], num_bins, retbins=True, labels=False, duplicates='drop')
    features['h1'] = h1
    h12, h12_bins = pd.qcut(features['h12'], num_bins, retbins=True, labels=False, duplicates='drop')
    features['h12'] = h12
    h123, h123_bins = pd.qcut(features['h123'], num_bins, retbins=True, labels=False, duplicates='drop')
    features['h123'] = h123
    h2_h1, h2_h1_bins = pd.qcut(features['h2_h1'], num_bins, retbins=True, labels=False, duplicates='drop')
    features['h2_h1'] = h2_h1
    return features, pi_bins, watterson_theta_bins, tajima_d_bins, h1_bins, h12_bins, h123_bins, h2_h1_bins

def save_bins(pi_bins, watterson_theta_bins, tajima_d_bins, h1_bins, h12_bins, h123_bins, h2_h1_bins, bin_output):
    df = pd.DataFrame()
    df['pi'] = pi_bins
    df['watterson_theta'] = watterson_theta_bins
    df['tajima_d'] = tajima_d_bins
    df['h1'] = h1_bins
    df['h12'] = h12_bins
    df['h123'] = h123_bins
    df['h2_h1'] = h2_h1_bins
    df.to_csv(bin_output)

def create_machine_learning_model_discretized(dir, model, output_name, test_output, roc_output, bin_output, num_bins):
    df = create_frame(dir)
    features = df.drop(['bs', 'bsb', 'left_window', 'right_window'], axis=1)

    binned, pi_bins, watterson_theta_bins, tajima_d_bins, h1_bins, h12_bins, h123_bins, h2_h1_bins = bin_data(features, num_bins)
    save_bins(pi_bins, watterson_theta_bins, tajima_d_bins, h1_bins, h12_bins, h123_bins, h2_h1_bins, bin_output)
    features = binned

    target = df['bsb']

    features_train, features_test, target_train, target_test = create_train_and_test_data(features, target, 1)

    model.fit(features_train, target_train)

    pred_test = model.predict(features_test)

    print('Accuracy:', calculate_accuracy(model, pred_test, target_test))
    print('Precision:', calculate_precision(model, pred_test, target_test))
    print('Recall:', calculate_recall(model, pred_test, target_test))
    print('F1:', calculate_f1(model, pred_test, target_test))

    plot_roc_curve(pred_test, target_test, roc_output)

    create_test_output(model, features_test, target_test, pred_test, test_output)

    joblib.dump(model, output_name)
