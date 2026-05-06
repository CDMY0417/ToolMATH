def verify_perfect_square(number: int):
    import math
    root = math.isqrt(number)
    return root if root * root == number else None
