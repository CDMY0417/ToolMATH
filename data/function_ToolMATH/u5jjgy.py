def integer_pairs_product(n: int):
    pairs = []
    for i in range(1, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            pairs.append((i, n // i))
            if i != n // i:
                pairs.append((-i, -(n // i)))
    return pairs
