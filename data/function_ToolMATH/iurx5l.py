def positive_even_perfect_cubes_below(limit: int) -> int:
    count = 0
    n = 1
    while (cube := (n * 2) ** 3) < limit:
        count += 1
        n += 1
    return count
