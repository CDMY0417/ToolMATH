def next_perfect_square(perfect_square: int) -> int:
    root = int(perfect_square**0.5)
    return (root + 1) ** 2
