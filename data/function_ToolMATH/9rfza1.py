def max_intersections_of_circles(n: int) -> int:
    from math import comb
    pairs = comb(n, 2)
    return pairs * 2
