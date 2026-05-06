def compound_interest_b(principal: float, rate: float, times_per_year: int, years: int) -> float:
    return principal * (1 + rate / times_per_year) ** (times_per_year * years)
