def is_perfect_square_r(x: int) -> bool:
    root = int(x**0.5)
    return root * root == x
