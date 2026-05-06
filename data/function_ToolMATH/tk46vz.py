def largest_power_less_than_d(base: int, number: int) -> int:
    power = 1
    while base ** power <= number:
        power += 1
    return power - 1
