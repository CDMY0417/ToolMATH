def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    return principal * (1 + rate) ** years
