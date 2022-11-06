import allel
import numpy as np

def calculate_summary_statistics(filename):
    """calculate the summary statistics from the vcf file

    Args:
        filename (String): the vcf file's name
    """
    vcf_dict = vcf_file_to_dict(filename)
    pi = calculate_pi(vcf_dict)
    watterson_theta = calculate_watterson_theta(vcf_dict)
    tajima_d = calculate_tajima_d(vcf_dict)
    print(pi)
    print(watterson_theta)
    print(tajima_d)

def vcf_file_to_dict(filename):
    """convert the vcf file to a dict

    Args:
        filename (String): the vcf file's name

    Returns:
        dict: the dict form of the vcf file
    """
    vcf_dict = allel.read_vcf(filename)
    return vcf_dict

def calculate_pi(vcf_dict):
    """calculates the pi summary statistic

    Args:
        vcf_dict (dict): the dict form of the vcf file

    Returns:
        float: the pi summary statistic
    """
    pos_ac_dict = get_pos_and_ac_from_vcf_dict(vcf_dict)
    pi, windows, n_bases, counts = allel.windowed_diversity(pos_ac_dict['pos'], pos_ac_dict['ac'], size=10, start=pos_ac_dict['pos'][0], stop=pos_ac_dict['pos'][-1])
    return pi

def calculate_watterson_theta(vcf_dict):
    """calculates the watterson theta summary statistic

    Args:
        vcf_dict (dict): the dict form of the vcf file

    Returns:
        float: the watterson theta summary statistic
    """
    pos_ac_dict = get_pos_and_ac_from_vcf_dict(vcf_dict)
    theta_hat_w, windows, n_bases, counts = allel.windowed_watterson_theta(pos_ac_dict['pos'], pos_ac_dict['ac'], size=10, start=pos_ac_dict['pos'][0], stop=pos_ac_dict['pos'][-1])
    return theta_hat_w

def calculate_tajima_d(vcf_dict):
    """calculates the tajima d summary statistic

    Args:
        vcf_dict (dict): the dict form of the vcf file

    Returns:
        float: the tajima d summary statistic
    """
    pos_ac_dict = get_pos_and_ac_from_vcf_dict(vcf_dict)
    D, windows, counts = allel.windowed_tajima_d(pos_ac_dict['pos'], pos_ac_dict['ac'], size=10, start=pos_ac_dict['pos'][0], stop=pos_ac_dict['pos'][-1])
    return D

def calculate_garud_h(vcf_dict):
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    h = g.to_haplotypes()
    return allel.moving_garud_h(h, 10)

def get_pos_and_ac_from_vcf_dict(vcf_dict):
    """gets the variant positions (pos) and the allele counts array (ac)

    Args:
        vcf_dict (dict): the dict form of the vcf file

    Returns:
        dict: the variant positions and the allele counts array returned as a dict
    """
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    ac = g.count_alleles()
    pos = vcf_dict['variants/POS']
    return {
        'pos': pos,
        'ac': ac
    }

calculate_summary_statistics('./vcf_files/vcfsectiontestssamplesize20')
def print_array(array):
    for thing in array:
        print(thing)

# vcf_dict = vcf_file_to_dict('./vcf_files/vcfsectiontestssamplesize20')
# g = allel.GenotypeArray(vcf_dict['calldata/GT'])
# ac = g.count_alleles()
# pos = vcf_dict['variants/POS']
# pos = allel.SortedIndex(pos, copy=False)
# ac = allel.asarray_ndim(ac, 2)
# an = np.sum(ac, axis=1)

# n_pairs = an * (an - 1) / 2

# n_same = np.sum(ac * (ac - 1) / 2, axis = 1)

# n_diff = n_pairs - n_same

# mpd = n_diff/n_pairs

# mpd_sum = np.sum(mpd)

# n_bases = pos[-1] - pos[0] + 1

# print(mpd_sum/n_bases)

