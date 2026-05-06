def calculate_compound_interest_total(principal: float, rate: float, time: int):
    total_payment = principal * (1 + rate) ** time
    return total_payment
