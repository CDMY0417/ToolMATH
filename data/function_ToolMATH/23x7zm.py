def smallest_multiplier_to_include_factors(a: int, b: int) -> int:
    def prime_factorization(n: int) -> dict:
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

    afactors = prime_factorization(a)
    bfactors = prime_factorization(b)

    x_factors = {}
    for p in bfactors:
        if p in afactors:
            if bfactors[p] > afactors[p]:
                x_factors[p] = bfactors[p] - afactors[p]
        else:
            x_factors[p] = bfactors[p]

    x = 1
    for p, power in x_factors.items():
        x *= p ** power

    return x
