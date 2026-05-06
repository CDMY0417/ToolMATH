def calculate_total_reduction(original_price: float, current_price: float) -> float:
    return (1 - current_price / original_price) * 100
