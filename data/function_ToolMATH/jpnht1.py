def perimeter_of_30_60_90_triangle(shortest_side: float) -> float:
    hypotenuse = 2 * shortest_side
    medium_side = shortest_side * (3**0.5)
    return shortest_side + hypotenuse + medium_side
