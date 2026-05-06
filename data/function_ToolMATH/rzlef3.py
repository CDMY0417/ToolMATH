def synthetic_division(coeffs: list[int], c: int):
    result = []
    carry = 0
    for coeff in coeffs:
        carry = coeff + carry * c
        result.append(carry)
    return result[:-1], result[-1]
