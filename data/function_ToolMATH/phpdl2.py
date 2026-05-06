def total_surface_area_open_box(edge_length: int) -> int:
    """Calculate the total external surface area of an open-top cubic box.

    Parameters:
    edge_length (int): The length of the edge of the square face of the box.

    Returns:
    int: The total surface area of the open-top box.
    """
    side_area = edge_length ** 2
    return 5 * side_area
