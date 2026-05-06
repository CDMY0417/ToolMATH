def is_perfect_square_ab(number: int) -> bool:
    root = int(number**0.5)
    return root * root == number
