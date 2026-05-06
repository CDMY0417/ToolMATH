def prime_factorization_bu(number: int):
    i = 2
    factors = {}
    while i * i <= number:
        while (number % i) == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            number //= i
        i += 1
    if number > 1:
        factors[number] = 1
    return factors
