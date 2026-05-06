def split_sum_into_parts(total_sum: int, num_terms: int) -> tuple:
    quotient = total_sum // num_terms
    remainder = total_sum % num_terms
    return quotient, remainder
