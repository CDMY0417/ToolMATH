def fraction_division(numerator: tuple, denominator: tuple) -> tuple:
    num = numerator[0] * denominator[1]
    den = numerator[1] * denominator[0]
    return (num, den)
