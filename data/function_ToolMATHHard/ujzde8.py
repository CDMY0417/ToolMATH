def count_integer_pairs_with_quadratic_constraints(R2: float, P: float, Q: float, amin: int, amax: int, bmin: int, bmax: int):
    """Return count of integer pairs (a,b) satisfying constraints within bounds."""
    count = 0
    for a in range(amin, amax + 1):
        for b in range(bmin, bmax + 1):
            s = a*a + b*b
            if s < R2 and s < P*a and s < Q*b:
                count += 1
    return count
