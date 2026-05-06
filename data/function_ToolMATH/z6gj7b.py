def integer_factorization_a(number: int) -> list[int]:
    factors = []
    divisor = 2
    while number >= divisor ** 2:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        factors.append(number)
    return factors
