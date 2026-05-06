def distribute_scalar_over_expression(scalar: int, binomial: tuple):
    term1, term2 = binomial
    return scalar * term1, scalar * term2
