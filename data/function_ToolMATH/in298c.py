def find_smallest_multiple(threshold: int, offset: int, divisor: int) -> int:
    n = threshold + 1
    while (n + offset) % divisor != 0:
        n += 1
    return n
