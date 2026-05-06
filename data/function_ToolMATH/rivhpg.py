def polynomial_long_division_c(dividend: list[float], divisor: list[float]):
    quotient = []
    remainder = dividend[:]
    divisor_degree = len(divisor) - 1
    divisor_lead_coef = divisor[0]
    while len(remainder) >= len(divisor) and remainder[0] != 0:
        lead_coef_quotient = remainder[0] / divisor_lead_coef
        degree_diff = len(remainder) - len(divisor)
        current_term = [0] * degree_diff + [lead_coef_quotient]
        quotient.append(lead_coef_quotient)
        subtract_term = [coef * lead_coef_quotient for coef in divisor] + [0]*degree_diff
        remainder = [rem - sub for rem, sub in zip(remainder, subtract_term)]
        while remainder and remainder[0] == 0:
            remainder.pop(0)
    return quotient, remainder
