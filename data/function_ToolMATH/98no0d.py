def is_divisible_by_l(tens_digit: int, units_digit: int) -> bool:
    return (tens_digit * 10 + units_digit) % 4 == 0
