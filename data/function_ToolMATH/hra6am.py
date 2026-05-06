def check_perfect_square(number: int) -> bool:
    root = int(number**0.5)
    return root * root == number
