def calculate_edges_in_prism(num_vertices: int):
    total_base_edges = num_vertices * 2
    connecting_edges = num_vertices
    total_edges = total_base_edges + connecting_edges
    return total_edges
