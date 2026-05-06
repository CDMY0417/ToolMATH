def multiply_fraction_to_power_of_ten(x: int, k: int):
    numerator = x * (5 ** k)
    denominator = 10 ** k
    return (numerator, denominator)
