def difference_of_sums(s1: str, s2: str, base1: int, base2: int) -> int:
    sum_base1 = int(s1, base1) + int(s2, base1)
    sum_base2 = int(s1, base2) + int(s2, base2)
    return sum_base1 - sum_base2
