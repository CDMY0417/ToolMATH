import math

def compute_4_pow_h_from_log_legs(dummy: int = 0):
    """Return 4^h with h = sqrt((log_4 27)^2 + (log_2 9)^2)."""
    L1 = math.log(27, 4)
    L2 = math.log(9, 2)
    h = math.hypot(L1, L2)
    return 4 ** h
