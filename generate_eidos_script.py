from script_initializer import initialize_script

def generate_eidos_script(filename, seed, mutation_rate):
    """
    Generates entire eidos script

    Args:
        filename (str): file to write to
        seed (int): seed for randomizer
        mutation_rate (float): mutation rate
    """
    with open(filename, "w") as script:
        script.write(initialize_script(seed, mutation_rate))

