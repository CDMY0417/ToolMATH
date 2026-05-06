def future_value(principal: float, rate: float, years: int) -> float:
    return principal * (1 + rate) ** years
