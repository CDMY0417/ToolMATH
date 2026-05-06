def required_principal_for_future_value(future_value: float, rate: float, years: int):
    return future_value / ((1 + rate) ** years)
