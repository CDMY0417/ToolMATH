def largest_power_less_equal(n: int, b: int) -> int:
    power = 1
    while power * b <= n:
        power *= b
    return power
