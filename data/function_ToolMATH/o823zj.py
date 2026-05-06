def bounce_height_after_bounces(initial_height: float, bounce_ratio: float, bounces: int):
    return initial_height * (bounce_ratio ** bounces)
