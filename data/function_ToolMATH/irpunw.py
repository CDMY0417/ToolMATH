def apply_am_gm_inequality_e(values: list[float]):
    n = len(values)
    if n == 0:
        return 0
    arithmetic_mean = sum(values) / n
    geometric_mean = 1
    for v in values:
        geometric_mean *= v ** (1/n)
    return arithmetic_mean, geometric_mean
