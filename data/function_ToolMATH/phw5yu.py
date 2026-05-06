def prime_factorization_bd(n: int) -> dict:
    factors = {}
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
    if n > 1:
        factors[n] = 1
    return factors
