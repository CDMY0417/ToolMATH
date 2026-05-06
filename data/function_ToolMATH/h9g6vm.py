def prime_factors_n(n: int):
    factors = []
    div = 2
    while n > 1:
        while n % div == 0:
            factors.append(div)
            n //= div
        div += 1
    return factors
