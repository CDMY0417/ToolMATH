def floor_sqrt_interval(n: int) -> tuple:
    lower_bound = n ** 2
    upper_bound = (n + 1) ** 2
    return (lower_bound, upper_bound)
