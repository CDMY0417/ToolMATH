def multiply_fractions_l(fraction1: tuple[int, int], fraction2: tuple[int, int]) -> tuple[int, int]:
    n1, d1 = fraction1
    n2, d2 = fraction2
    return (n1 * n2, d1 * d2)
