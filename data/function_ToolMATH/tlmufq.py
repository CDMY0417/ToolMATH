def generate_exponents_triples(max_value: int):
    return [(max_value, max_value, i) for i in range(max_value + 1)] + [(max_value, i, max_value) for i in range(max_value + 1)] + [(i, max_value, max_value) for i in range(max_value + 1)]
