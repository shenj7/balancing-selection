def initialize_script(seed: int, mutation_rate: float,
                      recombination_rate: float, selection_coefficient: str):
    """
    Initializes the eidos script

    Args:
        seed (float): randomizer seed
    """
    # TODO: what is the defineconstant?
    constant_l = 100
    return "initialize() {\n" \
        f"setSeed({seed});\ndefineConstant(\"L\", {constant_l});\n" \
        f"mutationMatrix = mmJukesCantor({mutation_rate});\n" \
        "initializeSLiMOptions(nucleotideBased=T);\ninitializeAncestralNucleotides(randomNucleotides(L));\n" \
        f"{generate_all_mutation_types(selection_coefficient)}\n" \
        f"{generate_all_genomic_element_types()}\n" \
        f"{generate_overall_genome()}\n" \
        f"{generate_recombination_rate(recombination_rate)}\n" \
        "}\n"


def generate_all_mutation_types(selection_coefficient):
    """
    Generates all mutations

    Returns:
        str: mutations
    """
    return generate_mutation_type("m1", "0.5", "f",
                                  "0.0") + generate_mutation_type(
                                      "m2", "0.5", "f", selection_coefficient)


def generate_mutation_type(mutation_name: str, dominance_coefficient: str,
                           fitness_type: str, fitness_parameter: str):
    """
    Generate mutation type

    Args:
        mutation_name (str): name of mutation
        dominance_coefficient (float): usually 0.5
        fitness_type (str): distribution of fitness effects
        fitness_parameter (float): fixed selection coefficient (0 for neutral, 0.1 for balancing)
    """
    return f"initializeMutationTypeNuc(\"{mutation_name}\", {dominance_coefficient}, " \
        f"\"{fitness_type}\", {fitness_parameter});\n"


def generate_all_genomic_element_types():
    return generate_genomic_element_type(
        "g1", "m1", "1.0") + generate_genomic_element_type(
            "g2", "c(m1, m2)", "c(999, 1)")


def generate_genomic_element_type(element_name: str, mutation_type: str,
                                  mutation_ratio: str):
    """
    Generate genomic element types

    Args:
        element_name (str): element name
        mutation_type (str): mutation type name (could be in a format such as c(m1, m2))
        mutation_ratio (str): mutation ratios (could be in a format such as c(0.2, 0.8))
    """
    return f"initializeGenomicElementType(\"{element_name}\", {mutation_type}, {mutation_ratio}, mutationMatrix);\n"


def generate_overall_genome():  #could make size an input
    # make random section generator that makes sections of a certain size
    start_index = 33  # will make random but hardcode for now
    end_index = 66
    return generate_genomic_element("g1", "0", str(start_index-1))\
        + generate_genomic_element("g2", str(start_index), str(end_index))\
            + generate_genomic_element("g1", str(end_index + 1), "99")


def generate_genomic_element(element_type: str, start: int, end: int):
    """
    Generates a section of a genome

    Args:
        element_type (str): name of genomic element type
        start (int): start of section
        end (int): end of section
    """
    return f"initializeGenomicElement({element_type}, {start}, {end});\n"


def generate_recombination_rate(rate: float):
    """
    Generates recombination rate

    Args:
        rate (float): recombination rate - usually should be small (0.01)
    """
    return f"initializeRecombinationRate({rate});\n"
