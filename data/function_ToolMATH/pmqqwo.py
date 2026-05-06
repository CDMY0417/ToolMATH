def square_monotonic_bounds(lower_bound: int, upper_bound: int):
    import math
    smallest = math.ceil(math.sqrt(lower_bound))
    largest = math.floor(math.sqrt(upper_bound))
    return smallest, largest
