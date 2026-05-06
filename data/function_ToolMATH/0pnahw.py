def sum_arithmetic_series_h(start: int, step: int, total_terms: int) -> int:
    end_term = start + step * (total_terms - 1)
    return total_terms * (start + end_term) // 2
