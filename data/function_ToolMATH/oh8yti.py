def calculate_number_of_recipes(total_items: int, items_per_recipe: int) -> int:
    import math
    return math.ceil(total_items / items_per_recipe)
