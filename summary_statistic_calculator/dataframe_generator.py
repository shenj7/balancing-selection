import pandas as pd
import calculations as calc
import os

def create_statistics_data_frame(vcf_dict, windowSize, balancing_left, balancing_right):
    """creates the dataframe of statistics

    Args:
        vcf_dict (_type_): _description_
        windowSize (_type_): _description_

    Returns:
        _type_: pandas DataFrame
    """
    windows, windowsl, windowsr = calc.calculate_windows(vcf_dict, windowSize)

    pi = calc.calculate_windowed_pi(vcf_dict, windows)
    theta_hat_w = calc.calculate_windowed_watterson_theta(vcf_dict, windows)
    D = calc.calculate_windowed_tajima_d(vcf_dict, windows)
    h1, h12, h123, h2_h1 = calc.calculate_windowed_garud_h(vcf_dict, windows)

    balancing_selection = calc.calculate_balancing_selection(windows, balancing_left, balancing_right)
    balancing_selection_binary = calc.calculate_balancing_selection_binary(windows, balancing_left, balancing_right)

    d = { 
          'Pi': pi, 
          'watterson_theta': theta_hat_w, 
          'tajima_d': D, 
          'h1': h1, 
          'h12': h12, 
          'h123': h123, 
          'h2_h1': h2_h1, 
          'bs': balancing_selection, 
          'bsb': balancing_selection_binary,
          'left_window': windowsl, 
          'right_window': windowsr 
          }

    df = pd.DataFrame(data=d)

    return df


def create_statistics_csv_from_file(vcf_file, windowSize, output, balancing_left, balancing_right):
    """creates the statistics csv

    Args:
        vcf_dict (_type_): _description_
        windowSize (_type_): _description_
        output (_type_): _description_
    """
    vcf_dict = calc.read_vcf(vcf_file)
    df = create_statistics_data_frame(vcf_dict, windowSize, balancing_left, balancing_right)
    df.to_csv(output)


def create_statistics_csv_from_directory(directory, windowSize, output, balancing_left, balancing_right):
    for filename in os.listdir(directory):
        vcf_dict = calc.read_vcf(directory + filename)
        df = create_statistics_data_frame(vcf_dict, windowSize, balancing_left, balancing_right)
        df.to_csv(output + filename[0:len(filename)-3] + 'csv')