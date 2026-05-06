def positive_intervals_rational_linear(num_roots, den_roots):
    """Return intervals where rational expression is positive."""
    roots = sorted(set(num_roots + den_roots))
    intervals = []
    # define sign function
    def sign_at(x):
        num = 1
        for r in num_roots:
            num *= (x - r)
        den = 1
        for r in den_roots:
            den *= (x - r)
        return num * den
    # intervals: (-inf, r1), (r1,r2), ... (rk, inf)
    bounds = [None] + roots + [None]
    for i in range(len(bounds)-1):
        low = bounds[i]
        high = bounds[i+1]
        # pick test point
        if low is None:
            test = high - 1
        elif high is None:
            test = low + 1
        else:
            test = (low + high) / 2.0
        if sign_at(test) > 0:
            intervals.append([low, high])
    return intervals
