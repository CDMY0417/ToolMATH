def count_arrangements_b(n: int, k: int) -> int:
    arrangements = 1
    for i in range(k):
        arrangements *= (n - i)
    return arrangements
