def count_distinct_sums_fixed_length(values, n: int):
    """Return count of distinct sums for length n using values with repetition."""
    if n < 0:
        raise ValueError("n must be nonnegative.")
    sums = {0}
    for _ in range(n):
        sums = {s + v for s in sums for v in values}
    return len(sums)
