def rational_roots_a(dividend_factors: list[int], divisor_factors: list[int]) -> set:
    roots = set()
    for m in dividend_factors:
        for n in divisor_factors:
            if n != 0:
                roots.add(m/n)
    return roots
