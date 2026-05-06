def slices_with_both_toppings_a(total_slices: int, topping1_slices: int, topping2_slices: int) -> int:
    n = (topping1_slices + topping2_slices) - total_slices
    return n
