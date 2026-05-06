def bounce_height(initial_height: float, bounce_coefficient: float, bounce_number: int) -> float:
    return initial_height * (bounce_coefficient ** bounce_number)
