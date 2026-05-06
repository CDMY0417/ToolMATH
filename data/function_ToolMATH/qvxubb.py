def cauchy_schwarz_inequality(seq1: tuple, seq2: tuple) -> float:
    sum_sq1 = sum(a**2 for a in seq1)
    sum_sq2 = sum(b**2 for b in seq2)
    sum_prod = sum(a*b for a, b in zip(seq1, seq2))
    return (sum_sq1 * sum_sq2) ** 0.5
