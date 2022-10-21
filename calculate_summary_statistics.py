import allel

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
    pi = allel.sequence_diversity(pos_ac_dict['pos'], pos_ac_dict['ac'])
    return pi

def calculate_watterson_theta(vcf_dict):
    """calculates the watterson theta summary statistic

    Args:
        vcf_dict (dict): the dict form of the vcf file

    Returns:
        float: the watterson theta summary statistic
    """
    pos_ac_dict = get_pos_and_ac_from_vcf_dict(vcf_dict)
    watterson_theta = allel.watterson_theta(pos_ac_dict['pos'], pos_ac_dict['ac'])
    return watterson_theta

def calculate_tajima_d(vcf_dict):
    """calculates the tajima d summary statistic

    Args:
        vcf_dict (dict): the dict form of the vcf file

    Returns:
        float: the tajima d summary statistic
    """
    pos_ac_dict = get_pos_and_ac_from_vcf_dict(vcf_dict)
    tajima_d = allel.tajima_d(pos_ac_dict['ac'], pos_ac_dict['pos'])
    return tajima_d



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