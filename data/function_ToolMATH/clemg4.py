def calculate_proportional_distance(current_distance: float, current_gallons: float, new_gallons: float):
    proportion = new_gallons / current_gallons
    return current_distance * proportion
