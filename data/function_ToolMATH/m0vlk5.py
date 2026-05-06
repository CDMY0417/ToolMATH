def calculate_inverted_proportion(initial_workers: int, initial_time: float, final_workers: int) -> float:
    constant = initial_workers * initial_time
    final_time = constant / final_workers
    return final_time
