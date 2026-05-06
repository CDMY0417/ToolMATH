def sum_of_two_longest(numbers: list[int]) -> int:
    return sum(sorted(numbers)[-2:])
