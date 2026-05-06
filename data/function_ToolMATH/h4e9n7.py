def check_isosceles_by_sides(sides: list[float]) -> bool:
    return len(set(sides)) == 2  # Two sides must be equal
