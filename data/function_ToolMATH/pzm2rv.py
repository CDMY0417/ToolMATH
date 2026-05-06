def factor_quadratic_u(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        # One way to factor the quadratic
        for p in range(1, a+1):
            if a % p == 0:
                r = a // p
                # Check all possible pairs (q, s) such that p*s + q*r = b
                for q in range(-c, c+1):
                    for s in range(-c, c+1):
                        if p*s + q*r == b and q*s == c:
                            return p, q, r, s
    return None
