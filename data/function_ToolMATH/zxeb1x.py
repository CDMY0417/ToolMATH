def bacteria_population_growth(initial_population: int, hours: int, doubling_rate: int):
    return initial_population * (doubling_rate ** hours)
