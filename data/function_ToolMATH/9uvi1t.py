def prime_factorization_factorial(n: int) -> dict:
    factors = {}
    for i in range(2, n + 1):
        num = i
        for p in range(2, i + 1):
            while num % p == 0:
                if p in factors:
                    factors[p] += 1
                else:
                    factors[p] = 1
                num //= p
    return factors
