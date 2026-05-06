def polynomial_long_division_b(dividend: list[float], divisor: list[float]) -> list[float]:
    quotient = []
    remainder = dividend[:]
    while len(remainder) >= len(divisor):
        lead_coeff = remainder[0] / divisor[0]
        quotient.append(lead_coeff)
        for i in range(len(divisor)):
            remainder[i] -= lead_coeff * divisor[i]
        remainder.pop(0)
    return quotient
