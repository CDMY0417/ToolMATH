def prime_factors_b(n: int) -> list:
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            if divisor not in factors:
                factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors
