def generate_even_pairs(max_even: int):
    return [(i, i+2) for i in range(2, max_even, 2)]
