def count_perfect_sixths(n: int) -> int:
    count = 0
    i = 1
    while i**6 <= n:
        count += 1
        i += 1
    return count
