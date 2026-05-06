def permutations_count(n: int):
    count = 1
    for i in range(1, n + 1):
        count *= i
    return count
