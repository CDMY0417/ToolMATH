def total_distance_traveled(initial_height: float, bounce_coefficient: float, num_bounces: int) -> float:
    descents = sum(initial_height * (bounce_coefficient ** i) for i in range(num_bounces))
    ascents = sum(initial_height * (bounce_coefficient ** (i + 1)) for i in range(num_bounces))
    return descents + ascents
