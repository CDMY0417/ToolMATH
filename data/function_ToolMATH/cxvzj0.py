def calculate_final_side_length(initial_length: int, increase_per_minute: int, minutes_elapsed: int) -> int:
    return initial_length + increase_per_minute * minutes_elapsed
