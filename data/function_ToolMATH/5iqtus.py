def prime_factors_f(num: int) -> dict:
    factors = {}
    d = 2
    while d * d <= num:
        while (num % d) == 0:
            num //= d
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
        d += 1
    if num > 1:
        factors[num] = 1
    return factors
