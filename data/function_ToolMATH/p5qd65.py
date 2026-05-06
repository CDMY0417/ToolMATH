def integer_congruence_count(m: int, c: int, k: int) -> int:
    count = 0
    n = 0
    while (k * n + c) <= m:
        if 1 <= (k * n + c) <= m:
            count += 1
        n += 1
    return count
