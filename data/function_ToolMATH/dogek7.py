def is_perfect_square_ai(num: int) -> bool:
    root = int(num ** 0.5)
    return root * root == num
