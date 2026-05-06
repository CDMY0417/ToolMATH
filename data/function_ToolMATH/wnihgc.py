def minimum_bounces_for_height(initial_height: float, bounce_ratio: float, target_height: float) -> int:
    bounces = 0
    height = initial_height
    while height >= target_height:
        bounces += 1
        height *= bounce_ratio
    return bounces
