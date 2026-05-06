def smallest_sixth_power_greater_than(num: int) -> int:
    base = 1
    while base ** 6 <= num:
        base += 1
    return base ** 6
