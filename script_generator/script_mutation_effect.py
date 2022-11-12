def add_mutation_effect(mutation_name: str, population_name: str):
    """
    Adds mutation effects to population and outputs each mutation

    Args:
        mutation_name (str): name of mutation effect
        population_name (str): name of population to apply mutation effect to

    Returns:
        _type_: _description_
    """
    # change lines 3 and 4 to same in the future - python currently shitting
    return f"mutationEffect({mutation_name})" \
            "{" \
            f"return 1.5 - sim.mutationFrequencies({population_name}, {mutation_name});"\
            "}"
    # what does the return statement do in mutationEffect?
