from machine_learning_model_generator import create_frame
import pandas as pd

def bin_data(features, bin_df):
    pi = pd.qcut(features['Pi'], bin_df['pi'], labels=False)
    features['Pi'] = pi
    watterson_theta = pd.qcut(features['watterson_theta'], bin_df['watterson_theta'], labels=False)
    features['watterson_theta'] = watterson_theta
    tajima_d = pd.qcut(features['tajima_d'], bin_df['tajima_d'], labels=False)
    features['tajima_d'] = tajima_d
    h1 = pd.qcut(features['h1'], bin_df['h1'], labels=False)
    features['h1'] = h1
    h12 = pd.qcut(features['h12'], bin_df['h12'], labels=False)
    features['h12'] = h12
    h123 = pd.qcut(features['h123'], bin_df['h123'], labels=False)
    features['h123'] = h123
    h2_h1 = pd.qcut(features['h2_h1'], bin_df['h2_h1'], labels=False)
    features['h2_h1'] = h2_h1
    return features

def model_predict(model, dir, bins):
    df = create_frame(dir)
    features = df.drop(['bs', 'bsb', 'left_window', 'right_window'], axis=1)
    if bins != None:
        bin_df = pd.read_csv(bins)
        features = bin_data(features, bin_df)
    
    pred = model.predict(features)