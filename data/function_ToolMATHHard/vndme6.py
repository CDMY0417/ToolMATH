def sum_f_pairwise_unit(N: int):
    """Return sum_{k=1}^{N-1} f(k/N)."""
    if N <= 1:
        return 0
    # pairs sum to 1
    return (N-1)//2
