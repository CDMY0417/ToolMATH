def count_specific_sum_pairs(list1: list[int], list2: list[int], target_sum: int) -> int:
    count = 0
    for x in list1:
        for y in list2:
            if x + y == target_sum:
                count += 1
    return count
