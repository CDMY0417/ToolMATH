def list_multiples_below_limit(base: int, limit: int):
    multiples = []
    current = base
    while current < limit:
        multiples.append(current)
        current += base
    return multiples
