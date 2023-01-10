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

def calculate_windowed_garud_h(vcf_dict, windows):
    """calculates the garud h statistics

    Args:
        vcf_dict (dictionary): the vcf file
        windows (array): the windows 

    Returns:
        h1 (ndarray): h1
        h12 (ndarray): h12
        h123 (ndarray): h123
        h1/h2 (ndarray): h1/h2
    """
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    hap = g.to_haplotypes()
    pos = vcf_dict['variants/POS']
    gh, windows, counts = allel.windowed_statistic(pos, hap, allel.garud_h, windows=windows)

    h1 = gh[:, 0]
    h12 = gh[:, 1]
    h123 = gh[:, 2]
    h2_h1 = gh[:, 3]
    return h1, h12, h123, h2_h1

def calculate_windowed_tajima_d(vcf_dict, windows):
    """calculates the windowed tajima d

    Args:
        vcf_dict (dict): the vcf dict
        windows (array): the windows 

    Returns:
        ndarray: tajima d
    """
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    ac = g.count_alleles()
    pos = vcf_dict['variants/POS']
    D, windows, counts = allel.windowed_tajima_d(pos, ac, windows=windows)
    return D

def calculate_windowed_pi(vcf_dict, windows):
    """calculates the windowed pi

    Args:
        vcf_dict (dict): the vcf dict
        windows (array): the windows 

    Returns:
        
    """
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    ac = g.count_alleles()
    pos = vcf_dict['variants/POS']
    pi, windows, n_bases, counts = allel.windowed_diversity(pos, ac, windows=windows)
    return pi

def calculate_windowed_watterson_theta(vcf_dict, windows):
    """calculates the windowed watterson theta

    Args:
        vcf_dict (dict): the vcf dict
        windows (array): the windows 

    Returns:
        
    """
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    ac = g.count_alleles()
    pos = vcf_dict['variants/POS']
    watterson_theta, windows, n_bases, counts = allel.windowed_watterson_theta(pos, ac, windows=windows)
    return watterson_theta

def calculate_balancing_selection(windows, balancing_left, balancing_right):
    """calculates the sections for balancing selection in the windows

    Args:
        windows (_type_): the windows that the summary statistics have been calculated in
        balancing_left (_type_): left starting point of balancing selection
        balancing_right (_type_): right ending point of balancing selection

    Returns:
        balancing_selection (array): the balancing_selection array
    """
    balancing_selection = []
    for window in windows:
        if window[1] < balancing_left or window[0] > balancing_right:
            balancing_selection.append(0)
        elif window[0] >= balancing_left and window[1] <= balancing_right:
            balancing_selection.append(1)
        else:
            balancing_selection.append(2)
    return balancing_selection

def calculate_windows(vcf_dict, windowSize):
    """calculate the windows

    Args:
        vcf_dict (dictionary): the vcf file
        windowSize (int): the window size

    Returns:
        array: left side of windows
        array: right side of windows
        array: windows
    """
    pos = vcf_dict['variants/POS']
    windows = []
    windowsl = []
    windowsr = []
    i = 0
    j = i + windowSize - 1
    if j >= len(pos):
        windowsl.append(pos[i])
        windowsr.append(pos[len(pos) - 1])
        windows.append([pos[i], pos[len(pos) - 1]])
    else:
        while j < len(pos):
            windowsl.append(pos[i])
            windowsr.append(pos[j])
            windows.append([pos[i], pos[j]])
            i += windowSize
            j += windowSize
        if i == len(pos) - 1:
            windowsr[len(windowsr) - 1] = pos[i]
            windows[len(windows) - 1][1] = pos[i]
        elif i < len(pos):
            windowsl.append(pos[i])
            windowsr.append(pos[len(pos) - 1])
            windows.append([pos[i], pos[len(pos) - 1]])
    return windows, windowsl, windowsr