def find_factor_pairs(n: int):
    pairs = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            pairs.append((i, n // i))
            pairs.append((-i, -n // i))
    return pairs
