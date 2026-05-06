def largest_power_less_than(base: int, number: int) -> int:
    power = 0
    while base ** (power + 1) < number:
        power += 1
    return base ** power
