import numpy as np
from pgmpy.inference.ExactInference import VariableElimination

class MyBayesianModel:
    def __init__(self, bs_model):
        self.bs_model = bs_model

    def fit(self, features, target):
        features['bsb'] = target
        self.bs_model.fit(features.reset_index())

    def predict(self, features):
        features = features.reset_index().drop(columns=['index'])
        model_infer = VariableElimination(self.bs_model)
        pred = []
        for index, row in features.iterrows():
            evidence = {'Pi': row['Pi'], 'watterson_theta': row['watterson_theta'], 'tajima_d': row['tajima_d'], 'h1': row['h1'], 'h12': row['h12'], 'h123': row['h123'], 'h2_h1': row['h2_h1']}
            inference = model_infer.map_query(['bsb'], evidence=evidence)
            pred.append(inference['bsb'])
        return np.asarray(pred)
        #return self.bs_model.predict(features)['bsb']
