def digit_sum_combinations_a(target_sum: int):
    combinations = []
    for i in range(10):
        for j in range(i, 10):
            if i + j == target_sum:
                combinations.append((i, j))
    return combinations
