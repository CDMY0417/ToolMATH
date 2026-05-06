def smallest_power_of_base_greater_than_value(base: int, value: int) -> int:
    power = 0
    while base ** power <= value:
        power += 1
    return power
