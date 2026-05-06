def count_perfect_cubes_a(n: int) -> int:
    count = 0
    i = 1
    while i * i * i <= n:
        count += 1
        i += 1
    return count
