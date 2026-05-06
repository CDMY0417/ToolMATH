def two_digit_factors(n: int):
    factors = []
    for i in range(10, 100):
        if n % i == 0:
            j = n // i
            if 10 <= j <= 99:
                factors.append((i, j))
    return factors
