def triangle_inequality_range(a: int, b: int) -> range:
    return range(abs(a-b) + 1, a+b)
