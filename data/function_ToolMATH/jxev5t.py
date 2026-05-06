def simplify_linear_equation(k: int, m: int, n: int, p: int) -> float:
    left_side = k - n
    right_side = p - m
    x = right_side / left_side
    return x
