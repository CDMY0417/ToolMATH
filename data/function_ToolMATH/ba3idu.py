def vieta_sums_for_cubic(a: int, b: int, c: int, d: int):
    roots_sum = -b / a
    roots_pairwise_sum = c / a
    roots_product = -d / a
    return roots_sum, roots_pairwise_sum, roots_product
