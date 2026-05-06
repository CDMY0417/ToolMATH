def range_of_square_function(c: float) -> tuple:
    # The minimum value of (x^2 + c)^2 is when x^2 = 0.
    min_value = c ** 2
    # The function can achieve all values greater than or equal to min_value.
    return (min_value, float('inf'))
