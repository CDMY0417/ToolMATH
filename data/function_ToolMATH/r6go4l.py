def multiples_overlap(list1: list[int], list2: list[int]) -> int:
    return len(set(list1) & set(list2))
