def calculate_compounded_amount(principal: float, rate: float, times_compounded: int) -> float:
    return principal * (1 + rate) ** times_compounded
