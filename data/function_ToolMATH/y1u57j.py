def two_digit_numbers_with_ones_digit(ones_digit: int) -> list:
    return [n for n in range(10, 100) if n % 10 == ones_digit]
