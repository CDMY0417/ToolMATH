def probability_successful_outcomes(successful_cases: int, total_cases: int) -> float:
    if total_cases == 0:
        return 0.0
    return successful_cases / total_cases
