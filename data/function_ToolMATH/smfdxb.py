def percent_without_conditions(total_surveyed: int, total_with_conditions: int) -> float:
    without_conditions = total_surveyed - total_with_conditions
    return (without_conditions / total_surveyed) * 100
