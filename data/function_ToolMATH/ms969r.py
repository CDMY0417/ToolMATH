def generate_arithmetic_sequence(a: int, d: int, limit: int):
    sequence = []
    n = 0
    while True:
        term = a + d * n
        if term >= limit:
            break
        sequence.append(term)
        n += 1
    return sequence
