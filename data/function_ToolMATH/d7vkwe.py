def calculate_discount_percentage(original_price: float, discounted_price: float) -> float:
    return 100 - (discounted_price / original_price * 100)
