def solve_linear_rational_inequality(a: float, b: float, c: float, d: float, e: float, f: float):
    """Return solution intervals for (x+a)/(x+b) > (c*x+d)/(e*x+f)."""
    # Bring to common denominator and solve sign.
    # (x+a)(e*x+f) - (c*x+d)(x+b) > 0
    A = e - c
    B = f + a*e - d - b*c
    C = a*f - b*d
    # Solve A x^2 + B x + C > 0 with poles at x=-b, x=-f/e
    # Compute roots
    roots = []
    if abs(A) < 1e-12:
        if abs(B) < 1e-12:
            return []
        r = -C / B
        roots = [r]
    else:
        disc = B*B - 4*A*C
        if disc >= 0:
            s = disc**0.5
            roots = [(-B - s)/(2*A), (-B + s)/(2*A)]
    poles = []
    poles.append(-b)
    if e != 0:
        poles.append(-f/e)
    points = sorted(set([p for p in poles + roots if p is not None]))
    # intervals from -inf to inf excluding points
    bounds = [None] + points + [None]
    intervals = []
    def sign_at(x):
        num = (x+a)*(e*x+f) - (c*x+d)*(x+b)
        den = (x+b)*(e*x+f)
        return num/den
    for i in range(len(bounds)-1):
        low, high = bounds[i], bounds[i+1]
        if low is None:
            test = high - 1
        elif high is None:
            test = low + 1
        else:
            test = (low + high)/2
        if sign_at(test) > 0:
            intervals.append([low, True if low is not None else False, high, True if high is not None else False])
    return intervals
