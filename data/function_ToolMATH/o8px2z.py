def largest_power_of_two_less_than(n: int) -> int:
    power, value = 0, 1
    while value * 2 <= n:
        power += 1
        value *= 2
    return power
