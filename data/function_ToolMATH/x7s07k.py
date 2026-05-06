def promotion_b_cost(first_item_price: float, discount: float) -> float:
    second_item_price = first_item_price - discount
    total_cost = first_item_price + second_item_price
    return total_cost
