import pandas as pd
import calculations as calc

def create_statistics_data_frame(vcf_dict, windowSize, balancing_left, balancing_right):
    """creates the dataframe of statistics

    Args:
        vcf_dict (_type_): _description_
        windowSize (_type_): _description_

    Returns:
        _type_: pandas DataFrame
    """

    pi, windows, n_bases, counts = calc.calculate_windowed_pi(vcf_dict, windowSize)
    h1, h12, h123, h2_h1, windows, counts = calc.calculate_windowed_garud_h(vcf_dict, windowSize, windows)
    d, windows, counts = calc.calculate_windowed_tajima_d(vcf_dict, windowSize, windows)
    theta_hat_w, windows, n_bases, counts = calc.calculate_windowed_watterson_theta(vcf_dict, windowSize, windows)
    balancing_selection = calc.calculate_balancing_selection(windows, balancing_left, balancing_right)
    windowsl, windowsr = calc.calculate_windows(windows)

    d = { 'Pi': pi, 
          'h1': h1, 
          'h12': h12, 
          'h123': h123, 
          'h2_h1': h2_h1, 
          'tajima_d': d, 
          'watterson_theta': theta_hat_w, 
          'bs': balancing_selection, 
          'left_window': windowsl, 
          'right_window': windowsr }

    df = pd.DataFrame(data=d)

    return df

def create_statistics_csv(vcf_file, windowSize, output, balancing_left, balancing_right):
    """creates the statistics csv

    Args:
        vcf_dict (_type_): _description_
        windowSize (_type_): _description_
        output (_type_): _description_
    """
    vcf_dict = calc.read_vcf(vcf_file)
    df = create_statistics_data_frame(vcf_dict, windowSize, balancing_left, balancing_right)
    df.to_csv(output)