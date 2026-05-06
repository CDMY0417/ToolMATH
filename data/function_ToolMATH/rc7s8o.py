def calculate_present_value(future_value: float, interest_rate: float, periods: int) -> float:
    return future_value / ((1 + interest_rate) ** periods)
