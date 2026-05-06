def calculate_original_price(sale_price: float, discount_percentage: float) -> float:
    original_price = sale_price / (1 - discount_percentage)
    return original_price
