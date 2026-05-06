def fibonacci_mod_m(limit: int, mod: int):
    if limit < 0:
        return []
    sequence = [0, 1]
    while len(sequence) < limit:
        sequence.append((sequence[-1] + sequence[-2]) % mod)
    return sequence[:limit]
