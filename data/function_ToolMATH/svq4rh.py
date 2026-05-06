def linear_arrangement_with_indistinguishable(total_items: int, counts: list[int]):
    from math import factorial
    denominator = 1
    for count in counts:
        denominator *= factorial(count)
    return factorial(total_items) // denominator
