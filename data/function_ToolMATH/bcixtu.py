def is_perfect_square_ag(n: int) -> bool:
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n
