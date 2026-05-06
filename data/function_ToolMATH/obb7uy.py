def prime_factorization_ay(n: int) -> dict:
    factors = {}
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factors[n] = 1
            break
    return factors
