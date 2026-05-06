def power_of_base_equals_n(n: int, b: int) -> bool:
    value = 1
    while value < n:
        value *= b
    return value == n
