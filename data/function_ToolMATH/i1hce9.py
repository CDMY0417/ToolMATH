def cost_for_number_of_items(original_items: int, original_cost: float, target_items: int) -> float:
    cost_per_item = original_cost / original_items
    return cost_per_item * target_items
