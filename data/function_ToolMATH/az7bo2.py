def calculate_simple_interest_total(principal: float, rate: float, time: int):
    interest_per_year = principal * rate
    total_interest = interest_per_year * time
    total_payment = principal + total_interest
    return total_payment
