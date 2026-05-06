def check_equality_condition(numbers: list[int]) -> bool:
    return len(set(numbers)) == 1 and all(n >= 0 for n in numbers)
