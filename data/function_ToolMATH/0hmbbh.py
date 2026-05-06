def units_digit_of_power_of_2(exponent: int) -> int:
    cycle = [2, 4, 8, 6]
    remainder = exponent % 4
    return cycle[remainder - 1]
