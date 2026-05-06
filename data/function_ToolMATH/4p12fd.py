def minimum_items_to_cover_cost(total_cost: int, net_income_per_item: int) -> int:
    return -(-total_cost // net_income_per_item)  # ceiling division
