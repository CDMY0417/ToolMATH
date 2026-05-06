def initial_investment(future_value: float, rate: float, years: int) -> float:
    return future_value / ((1 + rate) ** years)
