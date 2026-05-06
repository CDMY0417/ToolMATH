def indistinguishable_ball_arrangement(balls: int, boxes: int):
    import sympy
    partitions = sympy.partition(balls)
    unique_arrangements = [p for p in partitions if len(p) <= boxes]
    return len(unique_arrangements)
