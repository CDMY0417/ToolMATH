def cauchy_schwarz_inequality_a(sequence_a: list, sequence_b: list) -> bool:
    sum_a_sq = sum(x**2 for x in sequence_a)
    sum_b_sq = sum(y**2 for y in sequence_b)
    dot_product = sum(x * y for x, y in zip(sequence_a, sequence_b))
    return (sum_a_sq * sum_b_sq) >= (dot_product ** 2)
