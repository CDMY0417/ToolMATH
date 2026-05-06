def ratio_of_arithmetic_terms(a: int, d: int, n: int, m: int) -> float:
    term_n = a + (n - 1) * d
    term_m = a + (m - 1) * d
    return term_n / term_m if term_m != 0 else float('inf')
