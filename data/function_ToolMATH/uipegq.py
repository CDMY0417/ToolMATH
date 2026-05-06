def count_divisible_pairs(set_r: set[int], set_k: set[int]) -> int:
    count = 0
    for r in set_r:
        for k in set_k:
            if r % k == 0:
                count += 1
    return count
