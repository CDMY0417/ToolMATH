def count_multiples_in_grid(range1: list[int], range2: list[int], m: int) -> int:
    count = 0
    for i in range1:
        for j in range2:
            if (i * j) % m == 0:
                count += 1
    return count
