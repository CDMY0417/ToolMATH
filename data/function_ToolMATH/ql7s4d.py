def decompose_exponent(p: int, k: int):
    possible_pairs = []
    for d in range(1, k + 1):
        if k % d == 0:
            n = p ** (k // d)
            possible_pairs.append((n, d))
    return possible_pairs
