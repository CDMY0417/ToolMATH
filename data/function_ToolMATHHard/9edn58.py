def solve_rational_inequality_two_terms(p: float, q: float, r: float):
    """Return intervals for 1/(x+p) + q/(x+r) >= 1."""
    # Bring to common denominator and analyze sign of numerator over real line.
    # inequality: (x+r) + q(x+p) >= (x+p)(x+r)
    # => (1+q)x + (r+q*p) >= x^2 + (p+r)x + p*r
    # => 0 >= x^2 + (p+r-(1+q))x + (p*r - r - q*p)
    a = 1.0
    b = (p + r - (1.0 + q))
    c = (p*r - r - q*p)
    # Solve quadratic a x^2 + b x + c <= 0
    disc = b*b - 4*a*c
    if disc < 0:
        return []
    sqrt_disc = disc ** 0.5
    x1 = (-b - sqrt_disc) / (2*a)
    x2 = (-b + sqrt_disc) / (2*a)
    low, high = min(x1, x2), max(x1, x2)
    # Exclude poles x=-p and x=-r
    poles = sorted([-p, -r])
    intervals = []
    # candidate intervals from low to high, minus poles
    # a>0, so <=0 between roots
    # split by poles
    points = [low, high]
    segs = [low, high]
    # build open/closed intervals
    # start with [low, high], then remove poles
    segments = [[low, True, high, True]]  # inclusive at roots
    for pole in poles:
        new_segments = []
        for L, Li, H, Hi in segments:
            if pole <= L or pole >= H:
                new_segments.append([L, Li, H, Hi])
            else:
                new_segments.append([L, Li, pole, False])
                new_segments.append([pole, False, H, Hi])
        segments = new_segments
    return segments
