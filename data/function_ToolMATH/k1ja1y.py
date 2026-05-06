def smallest_congruent_in_range(value: int, m: int, low: int, high: int) -> int:
    n = value
    while n < low:
        n += m
    if n >= low and n < high:
        return n
    return None
