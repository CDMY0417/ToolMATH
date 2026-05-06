def sum_of_pyramid_edges(num_base_sides: int, base_side_length: float, slant_edge_length: float) -> float:
    perimeter_base = num_base_sides * base_side_length
    sum_slant_edges = num_base_sides * slant_edge_length
    return perimeter_base + sum_slant_edges
