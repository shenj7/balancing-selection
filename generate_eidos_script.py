def generate_eidos_script(filename, seed, mutation_rate):
    with open(filename, "w") as script:
        script.write(initialize_script(seed, mutation_rate))


def initialize_script(seed, mutation_rate):
    """
    Initializes the eidos script

    Args:
        seed (float): randomizer seed
    """
    return "initialize() {" \
        f"setSeed({mutation_name});initializeMutationRate{mutation_rate};"


def end_script()


def generate_mutation_type(mutation_name -> str, dominance_coefficient -> str,
    fitness_type -> str, fitness_parameter -> str):
    """
    Generate mutation type

    Args:
        mutation_name (str): name of mutation
        dominance_coefficient (float): usually 0.5
        fitness_type (str): distribution of fitness effects
        fitness_parameter (float): fixed selection coefficient (0 for neutral, 0.1 for balancing)
    """
    return f"initializeMutationType({mutation_name}, {dominance_coefficient}, " \ 
        f"{fitness_type}, {fitness_parameter}); "


def generate_genomic_element_type(element_name -> str, mutation_type -> str, mutation_ratio -> str):
    """
    Generate genomic element types

    Args:
        element_name (str): element name
        mutation_type (str): mutation type name (could be in a format such as c(m1, m2))
        mutation_ratio (str): mutation ratios (could be in a format such as c(0.2, 0.8))
    """
    return f"initializeGenomicElementType({element_name}, {mutation_type}, {mutation_ratio});"


def generate_overall_genome(size -> int):
    # make random section generator that makes sections of a certain size


def generate_genomic_element(element_type -> str, start -> int, end -> int):
    """
    Generates a section of a genome

    Args:
        element_type (str): name of genomic element type
        start (int): start of section
        end (int): end of section
    """
    return f"initializeGenomicElement({element_type}, {start}, {end});"


def add_population()


