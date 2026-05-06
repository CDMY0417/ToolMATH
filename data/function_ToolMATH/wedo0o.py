def sum_of_fractions(numerator: int, denominators: list[int]) -> float:
    return sum(numerator / d for d in denominators)
