def solve_sum_k2k_equals_power(m: int):
    """Return n satisfying sum_{k=2}^n k*2^k = 2^{n+m}."""
    # sum_{k=0}^n k*2^k = (n-1)2^{n+1}+2
    # sum_{k=2}^n = (n-1)2^{n+1}
    # (n-1)2^{n+1} = 2^{n+m} => n-1 = 2^{m-1}
    return 1 + 2**(m-1)
