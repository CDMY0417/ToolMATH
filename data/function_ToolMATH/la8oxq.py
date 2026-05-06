def count_perfect_squares_c(n: int) -> int:
    count = 0
    i = 1
    while i * i <= n:
        count += 1
        i += 1
    return count
