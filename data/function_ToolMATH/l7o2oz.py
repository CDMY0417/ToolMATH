def prime_factors_s(n: int):
    factors = []
    divisor = 2
    while n >= divisor * divisor:
        if n % divisor:
            divisor += 1
        else:
            n //= divisor
            factors.append(divisor)
    if n > 1:
        factors.append(n)
    return factors
