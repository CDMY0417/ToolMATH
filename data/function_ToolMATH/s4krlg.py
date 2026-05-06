def calculate_minimum_boxes(total_items: int, box_capacity: int):
    return (total_items + box_capacity - 1) // box_capacity
