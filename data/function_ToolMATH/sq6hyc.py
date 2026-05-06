def num_divisors(n: int) -> int:
    def prime_factor_exponents(n: int) -> list[int]:
        exponents = []
        d = 2
        while d * d <= n:
            count = 0
            while n % d == 0:
                n //= d
                count += 1
            if count > 0:
                exponents.append(count)
            d += 1
        if n > 1:
            exponents.append(1)
        return exponents
    exponents = prime_factor_exponents(n)
    result = 1
    for exp in exponents:
        result *= (exp + 1)
    return result
