def array_possibilities(integer: int):
    count = 0
    for i in range(2, integer // 2 + 1):
        if integer % i == 0:
            count += 1
    return count
