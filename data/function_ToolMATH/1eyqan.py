def recurrence_value(n: int, initial_values: list[int]) -> int:
    period = 10
    return initial_values[(n-1) % period]
