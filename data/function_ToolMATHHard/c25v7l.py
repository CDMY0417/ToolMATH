def smallest_integer_in_interval(a: float, b: float):
    # Smallest integer in (a,b)
    import math
    return math.floor(a) + 1 if a == int(a) else math.ceil(a)
