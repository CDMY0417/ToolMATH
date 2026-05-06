import math

def min_positive_a_from_vertex_and_integer_sum(h: float, k: float):
    """Return smallest positive a such that a+b+c is integer."""
    # a+b+c = a*(1-2h+h^2) + k
    coef = 1 - 2*h + h*h
    # find smallest positive a so coef*a + k is integer
    # Search m integers
    m = math.floor(coef*1 + k) - 2
    best = None
    for m in range(-10, 100):
        a = (m - k) / coef
        if a > 0:
            if best is None or a < best:
                best = a
    if best is None:
        raise ValueError("No positive a found.")
    return best
