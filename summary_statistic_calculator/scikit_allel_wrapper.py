import allel
import numpy as np
import pandas as pd

def read_vcf(input):
    """converts vcf file to a dict

    Args:
        input (string): filename

    Returns:
        dict: vcf in dict form
    """
    return allel.read_vcf(input)

def calculate_windowed_garud_h(vcf_dict, windowSize, windows):
    """calculates windowed garud statistics

    Args:
        vcf_dict (_type_): _description_
        windowSize (_type_): _description_
    
    Returns:

    """
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    hap = g.to_haplotypes()
    pos = vcf_dict['variants/POS']
    gh, windows, counts = allel.windowed_statistic(pos, hap, allel.garud_h, windowSize, windows=windows)

    h1 = gh[:, 0]
    h12 = gh[:, 1]
    h123 = gh[:, 2]
    h2_h1 = gh[:, 3]
    return h1, h12, h123, h2_h1, windows, counts

def calculate_windowed_tajima_d(vcf_dict, windowSize, windows):
    """calculates the windowed tajima d

    Args:
        vcf_dict (dict): the vcf dict
        windowSize (int): the size of the windows for the windowed statistic calculation

    Returns:
        ndarray: moving tajima d
    """
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    ac = g.count_alleles()
    pos = vcf_dict['variants/POS']
    d, windows, counts = allel.windowed_tajima_d(pos, ac, windowSize, windows=windows)
    return d, windows, counts

def calculate_windowed_pi(vcf_dict, windowSize):
    """calculates the windowed pi

    Args:
        vcf_dict (dict): the vcf dict
        windowSize (int): the size of the windows for the windowed statistic calculation

    Returns:
        
    """
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    ac = g.count_alleles()
    pos = vcf_dict['variants/POS']
    pi, windows, n_bases, counts = allel.windowed_diversity(pos, ac, size=windowSize)
    return pi, windows, n_bases, counts

def calculate_windowed_watterson_theta(vcf_dict, windowSize, windows):
    """calculates the windowed watterson theta

    Args:
        vcf_dict (dict): the vcf dict
        windowSize (int): the size of the windows for the windowed statistic calculation

    Returns:
        
    """
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    ac = g.count_alleles()
    pos = vcf_dict['variants/POS']
    watterson_theta, windows, n_bases, counts = allel.windowed_watterson_theta(pos, ac, windowSize, windows=windows)
    return watterson_theta, windows, n_bases, counts