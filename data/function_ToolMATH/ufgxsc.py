def expand_polynomial(p1: tuple[float, float, float], p2: tuple[float, float, float]) -> tuple[float, float, float, float, float]:
    c1, c2, c3 = p1
    d1, d2, d3 = p2
    return (
        c1 * d1,  # x^4 coefficient
        c1 * d2 + c2 * d1,  # x^3 coefficient
        c1 * d3 + c2 * d2 + c3 * d1,  # x^2 coefficient
        c2 * d3 + c3 * d2,  # x coefficient
        c3 * d3  # constant term
    )
