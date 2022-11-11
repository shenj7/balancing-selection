from uuid import uuid4

def finish_simulation(filepath: str, population: str):
    """
    Finish simulation

    Args:
        filepath (str): filepath to output to, default: ./{uuid4}
    """
    return "10000 late() {" \
        f"g = {population}.sampleIndividuals({sample_size}).genomes" \
        f"g.outputVCFSample(sampleSize={sample_size}, filePath=\"runs/{filepath or uuid4()}\");" \
        "sim.simulationFinished();}"
        