def factor_product(product: int) -> dict:
    factors = {}
    d = 2
    while product >= d * d:
        while (product % d) == 0:
            if d not in factors:
                factors[d] = 0
            factors[d] += 1
            product //= d
        d += 1
    if product > 1:
        factors[product] = 1
    return factors
