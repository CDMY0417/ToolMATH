def least_sixth_power_in_range(min_value: int, max_value: int):
    a = 1
    while True:
        power_six = a ** 6
        if power_six >= min_value and power_six <= max_value:
            return power_six
        elif power_six > max_value:
            return None
        a += 1
