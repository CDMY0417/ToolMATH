def scale_price_for_different_size(price: float, original_size: int, new_size: int) -> float:
    return price * (new_size / original_size)
