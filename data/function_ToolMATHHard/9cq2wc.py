def solve_p_q_orthogonal_equal_magnitude(a1: float, a3: float, b1: float, b2: float):
    'Solve p and q so vectors (a1,p,a3) and (b1,b2,q) are orthogonal and equal length.'
    # Orthogonality: a1*b1 + p*b2 + a3*q = 0 -> p*b2 + a3*q = -a1*b1
    # Equal lengths: a1^2 + p^2 + a3^2 = b1^2 + b2^2 + q^2 -> p^2 - q^2 = (b1^2 + b2^2) - (a1^2 + a3^2)
    if b2 == 0 or a3 == 0:
        raise ValueError('b2 and a3 must be nonzero for a unique solution')
    k1 = -a1 * b1
    delta = (b1*b1 + b2*b2) - (a1*a1 + a3*a3)
    # From linear equation: p = (k1 - a3*q) / b2
    # Substitute into p^2 - q^2 = delta -> quadratic in q
    # Solve: ((k1 - a3*q)/b2)^2 - q^2 = delta
    A = (a3*a3)/(b2*b2) - 1
    B = -2 * k1 * a3 / (b2*b2)
    C = (k1*k1)/(b2*b2) - delta
    if A == 0:
        q = -C / B
    else:
        disc = B*B - 4*A*C
        if disc < 0:
            raise ValueError('No real solution')
        # Choose one solution; both satisfy constraints.
        q = (-B + disc**0.5) / (2*A)
    p = (k1 - a3*q) / b2
    return [p, q]
