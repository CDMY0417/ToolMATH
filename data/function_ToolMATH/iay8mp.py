def triangle_area_l(base: int, side: int) -> float:
    half_base = base / 2
    # Calculate height using Pythagorean theorem
    height = (side**2 - half_base**2)**0.5
    # Area formula for triangle: 0.5 * base * height
    return 0.5 * base * height
