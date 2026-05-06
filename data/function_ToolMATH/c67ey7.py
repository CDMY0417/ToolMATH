def triangle_inequality_range_d(a: int, b: int) -> tuple[int, int]:
    lo = abs(a - b) + 1
    hi = a + b - 1
    return (lo, hi)
