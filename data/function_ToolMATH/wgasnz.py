def min_bounces_for_height(initial_height: float, bounce_ratio: float, target_height: float) -> int:
    k = 0
    while initial_height * (bounce_ratio ** k) >= target_height:
        k += 1
    return k
