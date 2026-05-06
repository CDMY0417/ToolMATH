def fraction_subtraction(numerator1: int, denominator1: int, numerator2: int, denominator2: int):
    lcm_denominator = denominator1 * denominator2
    num1 = numerator1 * denominator2
    num2 = numerator2 * denominator1
    return (num1 - num2), lcm_denominator
