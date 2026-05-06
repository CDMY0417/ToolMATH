def solve_abs_linear_rational_inequality(a: float, b: float, c: float, d: float, k: float):
    """Return intervals where |(a x + b)/(c x + d)| > k."""
    # Equivalent to (a x + b)^2 - k^2 (c x + d)^2 > 0
    A = a*a - k*k*c*c
    B = 2*a*b - 2*k*k*c*d
    C = b*b - k*k*d*d
    # Solve quadratic inequality A x^2 + B x + C > 0
    roots = []
    if abs(A) < 1e-12:
        if abs(B) < 1e-12:
            return []
        roots = [-C/B]
    else:
        disc = B*B - 4*A*C
        if disc >= 0:
            s = disc**0.5
            roots = [(-B - s)/(2*A), (-B + s)/(2*A)]
    # Exclude pole x = -d/c
    poles = []
    if c != 0:
        poles.append(-d/c)
    points = sorted(set([p for p in roots + poles if p is not None]))
    bounds = [None] + points + [None]
    intervals = []
    def sign_at(x):
        num = (a*x + b)
        den = (c*x + d)
        return (num/den)
    for i in range(len(bounds)-1):
        low, high = bounds[i], bounds[i+1]
        if low is None:
            test = high - 1
        elif high is None:
            test = low + 1
        else:
            test = (low + high)/2
        if abs(test + d/c) < 1e-9:
            test = test + 0.1
        if abs(sign_at(test)) > k:
            intervals.append([low, False, high, False])
    return intervals
