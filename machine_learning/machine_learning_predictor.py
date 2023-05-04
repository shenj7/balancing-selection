from machine_learning_model_generator import create_frame
import pandas as pd


def bin_data(features, pi_bins, watterson_theta_bins, tajima_d_bins, h1_bins, h12_bins, h123_bins, h2_h1_bins):
    pi = pd.cut(features['Pi'], pi_bins, labels=False, duplicates='drop')
    features['Pi'] = pi
    watterson_theta = pd.cut(features['watterson_theta'], watterson_theta_bins, labels=False, duplicates='drop')
    features['watterson_theta'] = watterson_theta
    tajima_d = pd.cut(features['tajima_d'], tajima_d_bins, labels=False, duplicates='drop')
    features['tajima_d'] = tajima_d
    h1 = pd.cut(features['h1'], h1_bins, labels=False, duplicates='drop')
    features['h1'] = h1
    h12 = pd.cut(features['h12'], h12_bins, labels=False, duplicates='drop')
    features['h12'] = h12
    h123 = pd.cut(features['h123'], h123_bins, labels=False, duplicates='drop')
    features['h123'] = h123
    h2_h1 = pd.cut(features['h2_h1'], h2_h1_bins, labels=False, duplicates='drop')
    features['h2_h1'] = h2_h1
    return features

def model_predict(model, dir, bins, prediction_location):
    df = create_frame(dir)
    features = df
    if bins != None:
        pi_bins = pd.read_csv(bins + '/pi_bins.csv')['pi']
        watterson_theta_bins = pd.read_csv(bins + '/watterson_theta_bins.csv')['watterson_theta']
        tajima_d_bins = pd.read_csv(bins + '/tajima_d_bins.csv')['tajima_d']
        h1_bins = pd.read_csv(bins + '/h1_bins.csv')['h1']
        h12_bins = pd.read_csv(bins + '/h12_bins.csv')['h12']
        h123_bins = pd.read_csv(bins + '/h123_bins.csv')['h123']
        h2_h1_bins = pd.read_csv(bins + '/h2_h1_bins.csv')['h2_h1']
        features = bin_data(features, pi_bins, watterson_theta_bins, tajima_d_bins, h1_bins, h12_bins, h123_bins, h2_h1_bins).dropna()
    features_copy = features.copy()
    features = features.drop(['bs', 'bsb', 'left_window', 'right_window'], axis=1)
    pred = model.predict(features)
    features_copy['pred'] = pred
    features_copy.to_csv(prediction_location)
    """df_pred = pd.DataFrame()
    df_pred['pred'] = pred
    df_pred['left_window'] = features_copy['left_window']
    df_pred['right_window'] = features_copy['right_window']
    df_pred.to_csv(prediction_location)"""
