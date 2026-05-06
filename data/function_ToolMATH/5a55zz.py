def next_multiple(a: int, b: int) -> int:
    return a if a % b == 0 else a + (b - a % b)
