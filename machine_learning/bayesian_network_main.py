from pgmpy.models import BayesianModel
# from pgmpy.factors.continuous.LinearGaussianCPD import LinearGaussianCPD
import sys
from machine_learning_model_generator import create_machine_learning_model
from machine_learning_model_generator import create_frame
from machine_learning_command_line_parser import command_line_parser
from pgmpy.inference.ExactInference import VariableElimination


class MyBayesianModel:
    def __init__(self, bs_model):
        self.bs_model = bs_model

    def fit(self, features, target):
        features['bsb'] = target
        self.bs_model.fit(features.reset_index())

    def predict(self, features):
        features = features.reset_index()
        model_infer = VariableElimination(self.bs_model)
        pred = []
        for index, row in features.iterrows():
            evidence = {'Pi': row['Pi'], 'watterson_theta': row['watterson_theta'], 'tajima_d': row['tajima_d'], 'h1': row['h1'], 'h12': row['h12'], 'h123': row['h123'], 'h2_h1': row['h2_h1']}
            inference = model_infer.map_query(['bsb'], evidence=evidence)
            pred.append(inference['bsb'])
        return pred


def create_bayesian_network(dir):
    df = create_frame(dir)

    bs_model = BayesianModel([('Pi', 'tajima_d'), ('watterson_theta', 'tajima_d'),
                              ('h1', 'h12'), ('h1', 'h123'), ('h1', 'h2_h1'), ('h12', 'h123'), ('h12', 'h2_h1'),
                              ('tajima_d', 'bsb'), ('h123', 'bsb'), ('h2_h1', 'bsb')])

    bs_model = MyBayesianModel(bs_model)
    # pi_cpd = LinearGaussianCPD('Pi', evidence_mean=df.mean()['Pi'], evidence_variance=df.mean()['Pi'])
    # tw_cpd = LinearGaussianCPD('TW', evidence_mean=df.mean()['watterson_theta'], evidence_variance=df.mean()['watterson_theta'])
    # dcpd = LinearGaussianCPD('D', evidence_mean=[df.mean()['tajima_d'], df.mean()['Pi'], df.mean()['watterson_theta']], evidence_variance=df.var()['tajima_d'], evidence=['Pi', 'TW'])
    # h1cpd = LinearGaussianCPD('H1', evidence_mean=df.mean()['h1'], evidence_variance=df.var()['h1'])
    # h12cpd = LinearGaussianCPD('H2', evidence_mean=[df.mean()['h2'], df.mean()['h1']], evidence_variance=df.var()['h2'], evidence=['H1'])
    # h123cpd = LinearGaussianCPD('H123', evidence_mean=[df.mean()['h123'], df.mean()['h1'], df.mean()['h12']], evidence_variance=df.var()['h123'], evidence=['H1', 'H12'])
    # h2_h1cpd = LinearGaussianCPD('H2_H1', evidence_mean=[df.mean()['h2_h1'], df.mean()['h1'], df.mean()['h12']], evidence_variance=df.var()['h2_h1'], evidence=['H1', 'H12'])
    # bscpd = LinearGaussianCPD('BS', evidence_mean=[df.mean()['bsb'], df.mean()['tajima_d'], df.mean()['h123'], df.mean()['h2_h1']], evidence_variance=df.var()['bsb'], evidence=['D', 'H123', 'H2_H1'])

    # bs_model.add_cpds(pi_cpd, tw_cpd, dcpd, h1cpd, h12cpd, h123cpd, h2_h1cpd, bscpd)


    return bs_model


def main(main_args=None):
    args = command_line_parser(main_args)

    bn = create_bayesian_network(args.directory)

    create_machine_learning_model(args.directory, bn, './generated_bayesian_networks/bn1.pkl', './generated_bayesian_networks/bn1.csv')

    # randomized_grid_search()


if __name__ == '__main__':
    main(sys.argv[1:])
