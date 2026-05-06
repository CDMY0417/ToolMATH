def count_combinations_h(total_value: int, denomination_values: list[int]):
    if total_value < 0:
        return 0
    if total_value == 0:
        return 1
    if not denomination_values:
        return 0
    first, *rest = denomination_values
    count = 0
    for i in range(total_value // first + 1):
        count += count_combinations(total_value - i * first, rest)
    return count
