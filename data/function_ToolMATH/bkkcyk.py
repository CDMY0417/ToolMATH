def count_factors_except_one(n: int) -> int:
    count = 0
    for i in range(2, n + 1):
        if n % i == 0:
            count += 1
    return count
