def total_cost_for_multiple(cost_for_n_items: float, num_items_n: int, desired_num_items: int) -> float:
    factor = desired_num_items / num_items_n
    return cost_for_n_items * factor
