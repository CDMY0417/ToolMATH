def digit_sum_combinations(digits: list[int], target: int):
    from itertools import combinations_with_replacement
    for count in range(1, target + 1):
        for combination in combinations_with_replacement(digits, count):
            if sum(combination) == target:
                yield combination
