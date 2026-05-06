def units_digit_of_power_a(base: int, power: int) -> int:
    if base % 10 == 0:
        return 0
    elif base % 10 == 1:
        return 1
    elif base % 10 == 5:
        return 5
    elif base % 10 == 6:
        return 6
    return pow(base % 10, power, 10)
