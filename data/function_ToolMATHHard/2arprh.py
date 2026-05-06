def evaluate_product_of_linear_rational_factors(x_values, numer_offsets, denom_offsets):
    """Return product of (x_i + p_i)/(x_i + q_i) across i."""
    if not (len(x_values) == len(numer_offsets) == len(denom_offsets)):
        raise ValueError("Input lists must have the same length.")
    prod = 1.0
    for x, p, q in zip(x_values, numer_offsets, denom_offsets):
        denom = x + q
        if denom == 0:
            raise ValueError("Denominator is zero.")
        prod *= (x + p) / denom
    return prod
