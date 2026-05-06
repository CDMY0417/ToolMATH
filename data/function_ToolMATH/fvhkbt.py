def find_exponent_for_terminating_decimal(five_power: int, two_power_current: int):
    if two_power_current < five_power:
        return five_power - two_power_current
    else:
        return 0
