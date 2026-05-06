import math

def centroid_distance_from_vertex(a: float, b: float, c: float):
    # Distance from vertex opposite side c to centroid = 2/3 of median to side c
    median = 0.5*math.sqrt(2*a*a + 2*b*b - c*c)
    return (2/3)*median
