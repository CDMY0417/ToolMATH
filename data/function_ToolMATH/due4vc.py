def lucas_sequence_modulo(length: int, mod: int):
    sequence = [1, 3]
    for _ in range(2, length):
        next_term = (sequence[-1] + sequence[-2]) % mod
        sequence.append(next_term)
    return sequence
