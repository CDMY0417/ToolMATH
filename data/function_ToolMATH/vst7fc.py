def find_proportional_quantity(ratio_item1: int, ratio_item2: int, quantity_item1: int) -> int:
    groups = quantity_item1 // ratio_item1
    return groups * ratio_item2
