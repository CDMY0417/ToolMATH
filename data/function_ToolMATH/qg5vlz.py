def divide_polynomials(numerator: list[float], denominator: list[float]):
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    remainder = numerator[:]
    normalizer = denominator[0]
    for i in range(len(quotient)):
        scale = remainder[i] / float(normalizer)
        quotient[i] = scale
        for j in range(len(denominator)):
            remainder[i + j] -= scale * denominator[j]
    return quotient, remainder
