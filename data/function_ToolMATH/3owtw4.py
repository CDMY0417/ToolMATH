def prime_factorization_exponents(n: int):
    exponents = {}
    factor = 2
    while n > 1:
        count = 0
        while n % factor == 0:
            n //= factor
            count += 1
        if count > 0:
            exponents[factor] = count
        factor += 1
    return exponents
