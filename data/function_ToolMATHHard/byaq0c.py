import math

def parallelogram_area_from_vectors_3d(v, w):
    # Area of parallelogram spanned by 3D vectors v and w
    cx = v[1]*w[2] - v[2]*w[1]
    cy = v[2]*w[0] - v[0]*w[2]
    cz = v[0]*w[1] - v[1]*w[0]
    return math.sqrt(cx*cx + cy*cy + cz*cz)
