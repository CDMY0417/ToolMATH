def compound_interest_quarterly(principal: float, annual_rate: float, years: int):
    quarterly_rate = annual_rate / 4
    total_periods = years * 4
    return principal * (1 + quarterly_rate) ** total_periods
