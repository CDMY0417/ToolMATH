def pair_and_count_condition(x: list[int], y: list[int]) -> int:
    return sum(1 for a in x for b in y if a > b)
