def solve_vector_from_dot_and_cross(a, dot: float, cross):
    # For a=(1,1,1): cross = (z-y, x-z, y-x)
    x = (dot - (cross[1]-cross[0]))/3
    y = x - cross[2]
    z = y + cross[0]
    return [x, y, z]
