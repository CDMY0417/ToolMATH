def factor_quartic_into_quadratics(a: int, b: int, c: int, d: int, e: int):
    """Brute-force integer factorization into two quadratics."""
    factors = []
    # possible integer factors for leading coeff and constant term
    lead = []
    for p in range(-abs(a), abs(a)+1):
        if p != 0 and a % p == 0:
            s = a // p
            lead.append((p, s))
    const = []
    for r in range(-abs(e), abs(e)+1):
        if r != 0 and e % r == 0:
            u = e // r
            const.append((r, u))
    for p,s in lead:
        for r,u in const:
            # solve for q,t using b and d
            # (px^2+qx+r)(sx^2+tx+u) -> coeffs:
            # x^3: p*t + q*s = b
            # x^1: q*u + r*t = d
            # x^2: p*u + q*t + r*s = c
            # brute q,t in range
            for qv in range(-50, 51):
                for tv in range(-50, 51):
                    if p*tv + qv*s != b:
                        continue
                    if qv*u + r*tv != d:
                        continue
                    if p*u + qv*tv + r*s != c:
                        continue
                    factors.append([[p,qv,r],[s,tv,u]])
    if not factors:
        raise ValueError("No integer quadratic factorization found.")
    # choose one with a<d in requested format
    for f in factors:
        if f[0][0] < f[1][0]:
            return f
    return factors[0]
