def cesaro_sum_with_prepended_one(C: float, n: int):
    """Return Cesaro sum for (1,a1..an) given Cesaro sum of (a1..an)."""
    # Sum of partial sums for n terms is C*n.
    total = C * n
    # New sum of partial sums: 1 + sum_{k=1}^{n} (1 + S_k) = 1 + n + total
    new_total = 1 + n + total
    return new_total / (n + 1)
