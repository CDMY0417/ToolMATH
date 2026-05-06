def factor_pairs_c(product: int):
    factors = []
    for i in range(1, int(abs(product) ** 0.5) + 1):
        if product % i == 0:
            factors.append((i, product // i))
            factors.append((-i, -(product // i)))
    return factors
