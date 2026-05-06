def ratio_to_roots(ratio: tuple, product: int):
    a, b = ratio
    root_2 = (product / a)**0.5
    root_1 = root_2 * a / b
    return root_1, root_2
