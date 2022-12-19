import pandas as pd
from pathlib import Path as pt
from sklearn.ensemble import RandomForestClassifier as rf

def create_frame(dir):
    files = pt(dir).glob("*")
    summary = None
    created = False
    for file in files:
        df = pd.read_csv(file)
        if not created:
            summary=df
        else:
            summary.append(df, ignore_index=True)

    return summary
        


def create_random_forest(dir):
    df = create_frame(dir)
    features = df.drop(['bs', 'left_window', 'right_window'], axis=1)
    target = df['bs']
    forest = rf()
    forest.fit(features, target)
    return forest