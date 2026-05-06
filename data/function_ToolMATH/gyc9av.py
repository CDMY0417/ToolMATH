def prime_factorization_cn(number: int) -> list:
    i = 2
    factors = []
    while i * i <= number:
        while (number % i) == 0:
            factors.append(i)
            number //= i
        i += 1
    if number > 1:
        factors.append(number)
    return factors
