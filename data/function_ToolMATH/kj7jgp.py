def integer_square_range(low: int, high: int):
    import math
    start = math.ceil(math.sqrt(low))
    end = math.floor(math.sqrt(high))
    return list(range(start, end + 1))
