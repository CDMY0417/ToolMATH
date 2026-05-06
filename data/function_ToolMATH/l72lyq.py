def floor_of_square_roots(n: int) -> list[int]:
    return [int(i**0.5) for i in range(1, n+1)]
