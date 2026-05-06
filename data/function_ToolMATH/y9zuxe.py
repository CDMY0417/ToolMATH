def calculate_full_recipes_needed(total_items: int, items_per_recipe: int):
    return (total_items + items_per_recipe - 1) // items_per_recipe
