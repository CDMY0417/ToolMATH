import math

def telescoping_log_sum(base: float, k_start: int, k_end: int):
    """Return the telescoping sum value."""
    if base <= 0 or base == 1:
        raise ValueError("Invalid base.")
    if k_start < 2 or k_end < k_start:
        raise ValueError("Invalid k range.")
    # sum becomes 1/log_base(k_start) - 1/log_base(k_end+1)
    logb = lambda x: math.log(x, base)
    return 1.0/logb(k_start) - 1.0/logb(k_end + 1)
