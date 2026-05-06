def square_area_from_perimeter(perimeter: int) -> int:
    side_length = perimeter / 4
    return int(side_length ** 2)
