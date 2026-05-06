def calculate_bottles_needed(total_volume_milliliters: float, bottle_capacity_milliliters: float) -> int:
    return -(-total_volume_milliliters // bottle_capacity_milliliters)
