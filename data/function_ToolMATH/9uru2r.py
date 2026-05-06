def multistage_selection_count(n: int, k: int):
    ways = 1
    for i in range(k):
        ways *= (n - i)
    return ways
