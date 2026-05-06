def is_divisible_by_last_digit(number: int) -> bool:
    units_digit = number % 10
    if units_digit == 0:
        return False
    return number % units_digit == 0
