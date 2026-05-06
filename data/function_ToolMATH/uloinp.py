def negative_multiples_above(k: int, limit: int):
    multiples = []
    n = -1
    while k * n > limit:
        multiples.append(k * n)
        n -= 1
    return multiples
