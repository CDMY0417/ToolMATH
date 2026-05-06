def find_integer_roots(coefficients: list[int], candidates: list[int]) -> list[int]:
    from numpy import poly1d
    p = poly1d(coefficients)
    integer_roots = [c for c in candidates if p(c) == 0]
    return integer_roots
