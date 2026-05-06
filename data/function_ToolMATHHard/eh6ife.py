def projection_matrix_missing_entries(b: float, d: float):
    # For projection matrix [[a,b],[c,d]], must be symmetric and trace=1 (rank 1)
    a = 1 - d
    c = b
    return [a, c]
