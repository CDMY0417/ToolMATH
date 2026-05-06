def pascal_triangle_coefficient(n: int, k: int) -> int:
    from math import comb
    return comb(n, k)
