def is_square_number(n: int) -> bool:
    root = int(n**0.5)
    return root * root == n
