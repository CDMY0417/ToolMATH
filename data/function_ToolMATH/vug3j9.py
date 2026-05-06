def integer_factor_pairs(n: int):
    factors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            factors.append((i, n // i))
            if i != n // i:  # Avoid duplicate pairs for square numbers
                factors.append((n // i, i))
    return factors
