def sum_of_squares_of_differences(number: float, values: list[float]) -> float:
    return sum((number - value) ** 2 for value in values)
