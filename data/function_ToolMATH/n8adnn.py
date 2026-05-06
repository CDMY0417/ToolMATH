def compound_interest_d(principal: float, rate: float, times_compounded: int, years: int) -> float:
    return principal * ((1 + rate / times_compounded) ** (times_compounded * years))
