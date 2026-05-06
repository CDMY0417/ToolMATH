def find_smallest_int_greater_than_product(value: int) -> int:
    n = int(value ** 0.5)
    while n * (n + 1) <= value:
        n += 1
    return n
