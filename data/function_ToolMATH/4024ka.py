def calculate_new_area(original_area: float, length_percentage_change: float, width_percentage_change: float):
    length_multiplier = 1 + length_percentage_change / 100
    width_multiplier = 1 + width_percentage_change / 100
    return original_area * length_multiplier * width_multiplier
