def add_population(name, size):
    """
    Adds population based off of initialize

    Args:
        name (str): name of population
        size (int): size of population
    """
    return "1 early() {\n" \
            f"sim.addSubpop({name}, {size});\n" \
            "}\n"