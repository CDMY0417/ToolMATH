def count_arrangements(n: int, k: int) -> int:
    arrangements = 1
    for i in range(n, n-k, -1):
        arrangements *= i
    return arrangements
