def ways_to_choose_successive_items(initial_count: int, chosen_count: int):
    result = 1
    for i in range(chosen_count):
        result *= (initial_count - i)
    return result
