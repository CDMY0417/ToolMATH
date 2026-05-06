def first_day_exceeding_population(initial_count: int, growth_rate: int, target: int) -> int:
    n = 0
    while initial_count * (growth_rate ** n) <= target:
        n += 1
    return n
