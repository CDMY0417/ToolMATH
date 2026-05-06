def apply_discount(original_price: float, discount_percent: float):
    discount_multiplier = (100 - discount_percent) / 100
    return original_price * discount_multiplier
