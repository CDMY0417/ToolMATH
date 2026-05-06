def polynomial_remainder_a(dividend: list[float], divisor: list[float]) -> list[float]:
    while len(dividend) >= len(divisor):
        leading_coeff_ratio = dividend[0] / divisor[0]
        term = [leading_coeff_ratio * x for x in divisor] + [0] * (len(dividend) - len(divisor))
        dividend = [a - b for a, b in zip(dividend, term)]
        dividend.pop(0)
    return dividend
