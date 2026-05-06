def first_three_digits_of_decimal(x: float):
    decimal_part = str(x).split('.')[1]
    return int(decimal_part[:3]) if len(decimal_part) >= 3 else int(decimal_part)
