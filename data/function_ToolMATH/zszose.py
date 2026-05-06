def is_perfect_square_af(number: int) -> bool:
    root = int(number**0.5)
    return number == root * root
