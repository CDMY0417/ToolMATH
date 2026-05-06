def integer_points_in_circle(radius: int) -> int:
    count = 0
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            if x**2 + y**2 <= radius**2:
                count += 1
    return count
