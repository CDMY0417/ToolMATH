def prime_factor_exponents_a(n: int, prime_factors: list[int]) -> list[int]:
    exponents = []
    for pf in prime_factors:
        count = 0
        while n % pf == 0:
            n //= pf
            count += 1
        exponents.append(count)
    return exponents
