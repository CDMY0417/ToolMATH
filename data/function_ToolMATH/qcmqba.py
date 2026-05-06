def product_greater_than_value(value: int) -> int:
    n = 1
    while n * (n + 1) <= value:
        n += 1
    return n
