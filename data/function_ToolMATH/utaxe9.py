def am_gm_inequality_h(values: list[float]) -> bool:
    import math
    n = len(values)
    return sum(values) / n >= math.prod(values) ** (1/n)
