def distinct_remainders_sum(max_value: int, modulus: int):
    remainders = set()
    for n in range(1, max_value + 1):
        remainders.add((n * n) % modulus)
    return sum(remainders)
