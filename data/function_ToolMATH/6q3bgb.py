def odd_perfect_squares_greater_than(limit: int):
    n = 1
    while n * n <= limit:
        n += 1
    while True:
        if n % 2 == 1:
            yield n * n
        n += 1
