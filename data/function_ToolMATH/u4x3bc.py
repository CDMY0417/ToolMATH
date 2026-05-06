def is_perfect_square_o(number: int) -> bool:
    if number < 0:
        return False
    root = int(number**0.5)
    return root * root == number
