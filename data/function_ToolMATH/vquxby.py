def multiply_chain_of_inequalities(inequalities: tuple, factor: float):
    return tuple(part * factor for part in inequalities)
