def calculate_30_60_90_triangle_sides(shortest_side_length: float):
    longer_leg = shortest_side_length * (3 ** 0.5)
    hypotenuse = 2 * shortest_side_length
    return longer_leg, hypotenuse
