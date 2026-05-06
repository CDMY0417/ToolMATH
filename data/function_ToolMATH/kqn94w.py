def is_perfect_square_in_range(start: int, end: int) -> bool:
    for n in range(int(start**0.5), int(end**0.5) + 1):
        if start <= n**2 < end:
            return True
    return False
