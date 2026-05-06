def group_by_digit_permutation(numbers: list[int]) -> list[list[int]]:
    from collections import defaultdict
    groups = defaultdict(list)
    for number in numbers:
        key = tuple(sorted(str(number)))
        groups[key].append(number)
    return list(groups.values())
