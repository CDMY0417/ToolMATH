def multiply_and_power_fractions(a: int, b: int, c: int, d: int, n: int):
    numerator = (a * c) ** n
    denominator = (b * d) ** n
    return (numerator, denominator)
