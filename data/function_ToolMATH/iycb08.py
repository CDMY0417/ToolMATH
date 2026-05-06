def largest_power_less_than_c(base: int, number: int) -> int:
    power = 0
    while base ** (power + 1) < number:
        power += 1
    return power
