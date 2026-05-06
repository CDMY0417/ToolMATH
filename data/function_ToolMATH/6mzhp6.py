def pythagorean_theorem_basic(side: int, hypotenuse: int) -> int:
    missing_side_square = hypotenuse**2 - side**2
    if missing_side_square > 0:
        return int(missing_side_square**0.5)
    return None
