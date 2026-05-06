def perfect_squares_up_to_a(max_value: int):
    return [i**2 for i in range(1, int(max_value**0.5) + 1)]
