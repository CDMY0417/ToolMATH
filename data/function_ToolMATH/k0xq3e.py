def reverse_growth(final_value: float, daily_growth_rate: float, days: int):
    initial_value = final_value / ((1 + daily_growth_rate) ** days)
    return initial_value
