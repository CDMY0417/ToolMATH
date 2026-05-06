def log_base_2_interval(lo: float, hi: float):
    assert 0 < lo <= hi, "Interval must be positive and non-empty"
    from math import log2
    return (log2(lo), log2(hi))
