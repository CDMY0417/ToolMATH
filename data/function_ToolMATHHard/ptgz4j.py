def min_max_overlap_counts(N: int, Amin: int, Amax: int, Bmin: int, Bmax: int):
    """Return [min_overlap, max_overlap, max_minus_min]."""
    min_inter = None
    max_inter = None
    for a in range(Amin, Amax + 1):
        for b in range(Bmin, Bmax + 1):
            min_i = max(0, a + b - N)
            max_i = min(a, b)
            if min_inter is None or min_i < min_inter:
                min_inter = min_i
            if max_inter is None or max_i > max_inter:
                max_inter = max_i
    return [min_inter, max_inter, max_inter - min_inter]
