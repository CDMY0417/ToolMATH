def two_digit_numbers_with_units_digit(units_digit: int):
    return [i for i in range(10, 100) if i % 10 == units_digit]
