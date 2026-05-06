def determine_common_difference(required_term: float, max_value: float, number_of_terms: int):
    max_common_difference_value = (max_value - required_term) / (number_of_terms - 1)
    return int(max_common_difference_value) if max_common_difference_value > 0 else None
