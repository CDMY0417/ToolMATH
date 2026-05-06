def split_decimal(number: float):
    integer_part = int(number)
    fractional_part = number - integer_part
    return integer_part, fractional_part
