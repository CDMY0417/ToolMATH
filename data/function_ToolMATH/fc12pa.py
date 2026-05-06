def generate_two_digit_numbers_with_units_digit(units_digit: int):
    return [n for n in range(10, 100) if n % 10 == units_digit]
