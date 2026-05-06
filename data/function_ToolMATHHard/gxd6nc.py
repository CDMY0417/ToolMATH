def evaluate_piecewise_rational_ab(a: float, b: float, threshold: float, p1: float, q1: float, r1: float, s1: float, p2: float, q2: float, r2: float, s2: float):
    """Evaluate the piecewise rational function."""
    if a + b <= threshold:
        denom = s1 * a
        if denom == 0:
            raise ValueError("Denominator is zero in first branch.")
        return (a*b + p1*a + q1*b + r1) / denom
    denom = s2 * b
    if denom == 0:
        raise ValueError("Denominator is zero in second branch.")
    return (a*b + p2*a + q2*b + r2) / denom
