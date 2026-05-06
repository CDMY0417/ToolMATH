def compound_interest_principal_to_future_value(principal: float, rate: float, years: int) -> float:
    return principal * ((1 + rate / 100) ** years)
