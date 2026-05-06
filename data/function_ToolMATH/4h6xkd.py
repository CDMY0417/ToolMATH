def sum_of_squares_given_sum_and_product(sum_ab: int, product_ab: int) -> int:
    squared_sum = sum_ab ** 2
    sum_of_squares = squared_sum - 2 * product_ab
    return sum_of_squares
