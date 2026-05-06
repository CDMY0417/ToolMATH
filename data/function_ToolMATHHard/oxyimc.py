def minpoly_sum_sqrts_value_at_one(a: float, b: float):
    """Return P(1) for minimal polynomial of sqrt(a)+sqrt(b)."""
    return 1 - 2*(a + b) + (a - b) * (a - b)
