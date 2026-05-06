def polynomial_division_b(dividend: list[float], divisor: list[float]) -> (list[float], list[float]):
    quotient = []
    remainder = dividend[:]
    divisor_degree = len(divisor) - 1
    divisor_lead_coeff = divisor[0]

    while len(remainder) >= len(divisor):
        lead_term_degree = len(remainder) - 1
        lead_term_coeff = remainder[0]
        term_degree = lead_term_degree - divisor_degree
        term_coeff = lead_term_coeff / divisor_lead_coeff
        quotient.append(term_coeff)

        for i in range(len(divisor)):
            remainder[i] -= term_coeff * divisor[i]

        remainder.pop(0)

    return quotient, remainder
