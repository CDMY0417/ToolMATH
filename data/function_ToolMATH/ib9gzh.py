def perfect_squares_up_to(n: int) -> list[int]:
    return [i**2 for i in range(1, int(n**0.5) + 1)]
