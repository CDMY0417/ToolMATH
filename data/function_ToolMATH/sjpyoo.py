def calculate_probability_n(specific_count: int, total_count: int) -> float:
    return specific_count / total_count if total_count > 0 else 0.0
