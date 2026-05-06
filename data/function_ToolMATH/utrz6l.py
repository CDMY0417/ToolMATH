def is_perfect_square_w(n: int) -> bool:
    root = int(n ** 0.5)
    return root * root == n
