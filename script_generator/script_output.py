from uuid import uuid4


def finish_simulation(filepath: str, population: str):
    """
    Finish simulation

    Args:
        filepath (str): filepath to output to, default: ./{uuid4}
    """
    sample_size = 20  # sample size for sampleIndividuals
    return "10000 late() {\n" \
        f"{population}.outputVCFSample(sampleSize={sample_size}, filePath=\"{filepath or uuid4()}\");" \
        "sim.simulationFinished();\n}\n"
        # f"g = {population}.sampleIndividuals({sample_size}).genomes;\n" \
        # f"g.outputVCF(filePath=\"{filepath or uuid4()}\", simplifyNucleotides=T);\n" \
        # "sim.simulationFinished();\n}\n"