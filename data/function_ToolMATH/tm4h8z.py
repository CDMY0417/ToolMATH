def integer_multiples_in_range_a(factor: float, start: float, end: float):
    n = 0
    multiples = []
    while factor * n <= end:
        if factor * n >= start:
            multiples.append(n)
        n += 1
    return multiples
