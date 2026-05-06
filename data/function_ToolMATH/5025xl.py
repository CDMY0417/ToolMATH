def bacteria_population(initial_count: int, growth_rate: int, days: int) -> int:
    return initial_count * (growth_rate ** days)
