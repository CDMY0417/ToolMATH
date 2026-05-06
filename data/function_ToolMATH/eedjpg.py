def compound_interest_c(principal: float, rate: float, years: int):
    compounded_amount = principal * (1 + rate) ** years
    return compounded_amount
