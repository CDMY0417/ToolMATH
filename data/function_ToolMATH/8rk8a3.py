def quadratic_solutions_less_than(c: int, target: int, threshold: int):
    import math
    solutions = []
    discriminant = target - c
    if discriminant < 0:
        return solutions
    root = math.sqrt(discriminant)
    candidates = [root, -root]
    for x in candidates:
        if x < threshold:
            solutions.append(x)
    return solutions
