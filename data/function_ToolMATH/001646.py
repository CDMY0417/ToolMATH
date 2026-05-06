def shaded_area(large_circle_area: float, small_circle_area: float, number_of_small_circles: int):
    return large_circle_area - (small_circle_area * number_of_small_circles)
