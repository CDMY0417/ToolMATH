def find_multiple_in_range_a(mult: int, low: int, high: int) -> int:
    for n in range((low // mult) + 1, (high // mult) + 1):
        return n * mult
    return None
