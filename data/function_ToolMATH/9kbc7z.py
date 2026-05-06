def calculate_initial_value(current_value: int, steps_to_initial: int) -> int:
    for _ in range(steps_to_initial):
        current_value //= 2
    return current_value
