from script_initializer import initialize_script
from script_add_population import add_population
from script_output import finish_simulation
from script_mutation_effect import add_mutation_effect

def generate_eidos_script(filename, seed, mutation_rate, recombination_rate, population_size, output_location):
    """
    Generates eidos script with random sections of
    balancing selection and neutral selection

    Args:
        filename (str): file to write to
        seed (int): seed for randomizer
        mutation_rate (float): mutation rate
    """
    popname = "p1"
    mut1 = "m1"
    mut2 = "m2"
    with open(f"test_runs/{filename}", "w") as script:
        script.write(initialize_script(seed, mutation_rate, recombination_rate))
        script.write(add_population(popname, population_size))  # how do we want to deal with population names
        add_mutation_effect(mut1, popname)
        add_mutation_effect(mut2, popname)
        script.write(finish_simulation(output_location, popname))


