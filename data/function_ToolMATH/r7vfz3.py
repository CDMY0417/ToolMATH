def cubic_power_sum(sum_of_numbers: int, product_of_numbers: int):
    a_plus_b = sum_of_numbers
    ab = product_of_numbers
    a_squared_plus_b_squared = a_plus_b**2 - 2 * ab
    a_cubed_plus_b_cubed = a_plus_b * a_squared_plus_b_squared - ab * a_plus_b
    return a_cubed_plus_b_cubed
