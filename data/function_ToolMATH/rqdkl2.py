def calculate_new_average(current_total: int, current_count: int, additional_value: int) -> float:
    new_total = current_total + additional_value
    new_count = current_count + 1
    return new_total / new_count
