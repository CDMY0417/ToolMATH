def polynomial_long_division_d(dividend: list[float], divisor: list[float]) -> list[float]:
    quotient = []
    dividend_copy = dividend[:]
    while len(dividend_copy) >= len(divisor):
        lead_coeff_quotient = dividend_copy[0] / divisor[0]
        quotient.append(lead_coeff_quotient)
        subtrahend = [lead_coeff_quotient * d for d in divisor]
        dividend_copy = [a - b for a, b in zip(dividend_copy, subtrahend)] + dividend_copy[len(subtrahend):]
        while dividend_copy and dividend_copy[0] == 0:
            dividend_copy.pop(0)
    return quotient
