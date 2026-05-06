def smallest_positive_solution(constant: float, coefficient: float) -> float:
    import math
    k = 0
    while True:
        x = (k * math.pi + constant) / coefficient
        if x > 0:
            return x
        k += 1
