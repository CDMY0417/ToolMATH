def am_gm_inequality_b(values: list[float]):
    n = len(values)
    geometric_mean = 1
    for value in values:
        geometric_mean *= value
    geometric_mean = geometric_mean ** (1/n)
    arithmetic_mean = sum(values) / n
    return arithmetic_mean, geometric_mean
