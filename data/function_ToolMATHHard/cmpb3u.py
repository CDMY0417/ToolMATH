import math

def solve_symmetric_quartic(K: float):
    """Return real solutions for x^4+(2-x)^4=K."""
    # Let u = x-1 => equation 2(u^4+6u^2+1)=K
    rhs = K/2.0 - 1.0
    # u^4 + 6u^2 - rhs = 0 => v^2 + 6v - rhs = 0 with v=u^2
    disc = 36 + 4*rhs
    if disc < 0:
        return []
    v1 = (-6 + math.sqrt(disc))/2.0
    v2 = (-6 - math.sqrt(disc))/2.0
    sols = []
    for v in [v1, v2]:
        if v >= 0:
            u = math.sqrt(v)
            sols.append(1 - u)
            sols.append(1 + u)
    sols = sorted(set([round(s,12) for s in sols]))
    return sols
