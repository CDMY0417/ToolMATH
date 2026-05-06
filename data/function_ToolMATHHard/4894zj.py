import math

def solve_positive_triple_from_pairwise_products(xy: float, xz: float, yz: float):
    """Return [x,y,z] for positive x,y,z."""
    if xy <= 0 or xz <= 0 or yz <= 0:
        raise ValueError("Inputs must be positive.")
    x = math.sqrt(xy * xz / yz)
    y = xy / x
    z = xz / x
    return [x, y, z]
