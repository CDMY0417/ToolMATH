def alternating_sum_of_series(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum -= i
        else:
            sum += i
    return sum
