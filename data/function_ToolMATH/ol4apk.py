def prime_factorization_az(number: int):
    factors = {}
    d = 2
    while d * d <= number:
        while number % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            number //= d
        d += 1
    if number > 1:
        factors[number] = 1
    return factors
