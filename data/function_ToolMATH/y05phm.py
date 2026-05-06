def annual_compounded_balance(principal: float, rate: float, years: int) -> float:
    return principal * (1 + rate) ** years
