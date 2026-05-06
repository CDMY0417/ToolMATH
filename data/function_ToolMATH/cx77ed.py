def sum_fractions(fraction1: tuple[int, int], fraction2: tuple[int, int]) -> tuple[int, int]:
    num1, denom1 = fraction1
    num2, denom2 = fraction2
    common_denom = denom1 * denom2
    num_sum = num1 * denom2 + num2 * denom1
    return num_sum, common_denom
