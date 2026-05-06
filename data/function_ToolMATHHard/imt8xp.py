def transform_expression_with_reciprocal(S: float):
    """Given S = x + sqrt(x^2-1) + 1/(x - sqrt(x^2-1)) = 2t, return t^2 + 1/t^2."""
    t = S / 2.0
    return t*t + 1.0/(t*t)
