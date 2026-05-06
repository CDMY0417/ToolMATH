def product_of_coordinates(coordinates: tuple[float, ...]) -> float:
    product = 1
    for coordinate in coordinates:
        product *= coordinate
    return product
