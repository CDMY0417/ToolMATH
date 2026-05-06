def find_smallest_greater_than(base: int, step: int, minimum: int) -> int:
    a = (minimum - base + step) // step
    return base + step * a
