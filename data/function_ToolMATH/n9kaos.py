def sum_of_squares_equal_sum(numbers: list[float]) -> bool:
    total_sum = sum(numbers)
    sum_of_squares = sum(x**2 for x in numbers)
    return total_sum == sum_of_squares
