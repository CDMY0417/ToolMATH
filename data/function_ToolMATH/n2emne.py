def calculate_odd_perfect_square_above_threshold(threshold: int) -> int:
    n = int(threshold ** 0.5) + 1
    if n % 2 == 0:
        n += 1
    return n * n
