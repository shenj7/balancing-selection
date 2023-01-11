import pandas as pd
from pathlib import Path as pt
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
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

def calculate_accuracy(forest, features_test, target_test):
    return accuracy_score(target_test, forest.predict(features_test))

def calculate_precision(forest, features_test, target_test):
    return precision_score(target_test, forest.predict(features_test), average='micro')

def calculate_recall(forest, features_test, target_test):
    return recall_score(target_test, forest.predict(features_test), average='micro')

def calculate_f1(forest, features_test, target_test):
    return f1_score(target_test, forest.predict(features_test), average='micro')

def create_random_forest(dir):
    df = create_frame(dir)

    features = df.drop(['bs', 'left_window', 'right_window'], axis=1)
    target = df['bs']

    features_train, features_test, target_train, target_test = create_train_and_test_data(features, target, 0)

    forest = rf()
    forest.fit(features_train, target_train)
    print(forest.predict(features_test))
    
    print(calculate_accuracy(forest, features_test, target_test))
    print(calculate_precision(forest, features_test, target_test))
    print(calculate_recall(forest, features_test, target_test))
    print(calculate_f1(forest, features_test, target_test))

    joblib.dump(forest, './generated_forests/forest1.pkl')

    return forest