def multiply_fractions_h(fraction1: tuple[int, int], fraction2: tuple[int, int]) -> tuple[int, int]:
    num1, den1 = fraction1
    num2, den2 = fraction2
    num = num1 * num2
    den = den1 * den2
    return (num, den)
