def square_of_difference_of_exponentials(value: float) -> float:
    import math
    return (math.exp(value) - math.exp(-value)) ** 2
