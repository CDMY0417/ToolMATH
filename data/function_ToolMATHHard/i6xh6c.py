def sum_of_squared_norms_from_midpoint_and_dot(m, dot_ab: float):
    # Compute |a|^2 + |b|^2 from midpoint m=(a+b)/2 and dot a·b
    s = 0.0
    for x in m:
        s += (2*x) * (2*x)
    return s - 2*dot_ab
