def factor_out_constant(terms: list[float], constant: float):
    return [term / constant for term in terms]
