def solve_vector_from_two_projections(p1, proj1, p2, proj2):
    x = proj1[0]
    dot = proj2[0]*p2[0] + proj2[1]*p2[1]
    y = (dot - x) / p2[1]
    return [x, y]
