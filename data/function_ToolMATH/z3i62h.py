def multiply_fractions_w(fraction1: tuple[int, int], fraction2: tuple[int, int]) -> tuple[int, int]:
    numerator = fraction1[0] * fraction2[0]
    denominator = fraction1[1] * fraction2[1]
    return (numerator, denominator)
