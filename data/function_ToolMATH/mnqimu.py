def evaluate_power_of_fraction(numerator: int, denominator: int, power: int):
    result = (numerator / denominator) ** power
    integer_part = int(result)
    fractional_part = result - integer_part
    return integer_part, fractional_part
