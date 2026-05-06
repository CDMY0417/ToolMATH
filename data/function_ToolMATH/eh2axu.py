def multiply_by_power_of_ten(numerator: int, denominator: int, power: int):
    factor = 10 ** power
    return numerator * factor, denominator * factor
