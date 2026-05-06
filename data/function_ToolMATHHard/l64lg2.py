def cubic_interpolation_value(v1: float, v2: float, v3: float, v4: float):
    """Return p(5) for cubic interpolating (1,v1)..(4,v4)."""
    xs = [1,2,3,4]
    vs = [v1,v2,v3,v4]
    # Lagrange interpolation at x=5
    x0 = 5
    total = 0.0
    for i in range(4):
        num = 1.0
        den = 1.0
        for j in range(4):
            if i==j:
                continue
            num *= (x0 - xs[j])
            den *= (xs[i] - xs[j])
        total += vs[i] * num / den
    return total
