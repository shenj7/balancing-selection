import allel
import numpy as np

def read_vcf(input):
    return allel.read_vcf(input)

def calculate_moving_garud_h(vcf_dict, windowSize):
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    hap = g.to_haplotypes()
    h1, h12, h123, h2_h1 = allel.moving_garud_h(hap, windowSize)
    return h1, h12, h123, h2_h1

def calculate_moving_tajima_d(vcf_dict, windowSize):
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    ac = g.count_alleles()
    d = allel.moving_tajima_d(ac, windowSize)
    return d

def calculate_moving_pi(vcf_dict, windowSize):
    g = allel.GenotypeArray(vcf_dict['calldata/GT'])
    ac = g.count_alleles()
    mpd = allel.mean_pairwise_difference(ac)
    mpd_sum = allel.moving_statistic(mpd, np.sum, windowSize)
    return mpd_sum

def main():
    vcf_dict = read_vcf('./vcf_files/vcfsectiontestssamplesize20')
    windowSize = 10
    h1, h12, h123, h2_h1 = calculate_moving_garud_h(vcf_dict, windowSize)
    d = calculate_moving_tajima_d(vcf_dict, windowSize)
    pi = calculate_moving_pi(vcf_dict, windowSize)
    print(h1, '\n')
    print(h12, '\n')
    print(h123, '\n')
    print(h2_h1, '\n')
    print(d, '\n')
    print(pi, '\n')

main()