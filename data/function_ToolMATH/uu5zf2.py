def find_dimensions_with_perimeter(perimeter: int) -> list:
    dimensions = []
    for width in range(1, perimeter // 2):
        length = (perimeter // 2) - width
        if length >= width:
            dimensions.append((length, width))
    return dimensions
