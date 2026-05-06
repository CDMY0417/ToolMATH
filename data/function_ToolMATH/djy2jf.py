def factorize_number_c(number: int):
    factors = []
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors
