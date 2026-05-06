def sum_cos_sin_ratio(n: int):
    import math
    A = sum(math.cos(math.radians(i)) for i in range(1, n + 1))
    B = sum(math.sin(math.radians(i)) for i in range(1, n + 1))
    return A / B
