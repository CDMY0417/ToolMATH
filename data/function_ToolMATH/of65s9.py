def factorial_prime_factorization_a(n: int):
    factors = {}
    for i in range(2, n + 1):
        num = i
        d = 2
        while num > 1:
            count = 0
            while num % d == 0:
                num //= d
                count += 1
            if count > 0:
                if d in factors:
                    factors[d] += count
                else:
                    factors[d] = count
            d += 1
    return factors
