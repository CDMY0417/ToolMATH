def price_by_volume(initial_price: float, old_volume: float, new_volume: float) -> float:
    ratio = new_volume / old_volume
    return initial_price * ratio
