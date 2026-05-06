def fraction_of_integers_divisible_by_3(start: int, end: int) -> float:
    total = end - start + 1
    divisible_count = sum(1 for i in range(start, end + 1) if i % 3 == 0)
    return divisible_count / total
