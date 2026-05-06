def slices_with_both_toppings(total_slices: int, pepperoni_slices: int, mushroom_slices: int) -> int:
    overlap_slices = pepperoni_slices + mushroom_slices - total_slices
    return overlap_slices
