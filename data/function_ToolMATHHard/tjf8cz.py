def min_sum_reciprocals_given_sum(n: int, S: float):
    """Return minimum sum of reciprocals using Cauchy: n^2/S."""
    if n <= 0 or S <= 0:
        raise ValueError("n and S must be positive.")
    return (n*n) / S
