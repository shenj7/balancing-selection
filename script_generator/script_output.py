from uuid import uuid4

def finish_simulation(filepath: str, population: str):
    """
    Finish simulation

    Args:
        filepath (str): filepath to output to, default: ./{uuid4}
    """
    return "10000 early() { sim.simulationFinished();" \
        f"{population}.genomes.outputVCF(filePath=\"runs/{filepath or uuid4()}\");" \
        "}"
        