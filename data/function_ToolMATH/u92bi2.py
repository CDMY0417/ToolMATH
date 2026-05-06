def ways_to_permute_with_repeats(total_items: int, repeats: list[int]):
    from math import factorial
    denominator = 1
    for r in repeats:
        denominator *= factorial(r)
    return factorial(total_items) // denominator
