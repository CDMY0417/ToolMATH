def solve_for_annual_interest_rate(principal: float, future_value: float, years: int) -> float:
    rate_factor = (future_value / principal) ** (1 / years)
    return (rate_factor - 1) * 100
