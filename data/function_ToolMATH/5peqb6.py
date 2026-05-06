def possible_sum_pairs(target: int):
    return [(x, target - x) for x in range(target + 1)]
