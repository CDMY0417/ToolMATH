def largest_power_less_than_a(base: int, n: int) -> int:
    k = 0
    power_value = 1
    while power_value * base <= n:
        k += 1
        power_value *= base
    return k
