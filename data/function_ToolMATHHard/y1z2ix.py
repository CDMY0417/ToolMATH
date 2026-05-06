def solve_two_term_rational_equation_reducible(a1,b1,c1,d1,e1,a2,b2,c2,d2,e2,k):
    """Solve when each quadratic term divides cleanly by its linear denominator."""
    # polynomial division for (a*y^2+b*y+c) / (d*y+e) -> (p*y+q) remainder r
    def divide_quadratic(a,b,c,d,e):
        if d == 0:
            raise ValueError("d must be nonzero.")
        p = a / d
        q = (b - p * e) / d
        r = c - q * e
        return (p, q, r)
    p1, q1, r1 = divide_quadratic(a1,b1,c1,d1,e1)
    p2, q2, r2 = divide_quadratic(a2,b2,c2,d2,e2)
    if abs(r1) > 1e-9 or abs(r2) > 1e-9:
        raise ValueError("Terms are not divisible; not reducible.")
    # equation: (p1*y+q1) + (p2*y+q2) = k
    A = p1 + p2
    B = q1 + q2 - k
    if abs(A) < 1e-12:
        raise ValueError("No unique solution.")
    return [-B / A]
