def days_multiple_of_k_in_month(k: int, total_days: int):
    return [day for day in range(1, total_days + 1) if day % k == 0]
