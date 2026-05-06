def polygon_area_by_difference(large_area: float, subtract_areas: list[float]) -> float:
    return large_area - sum(subtract_areas)
