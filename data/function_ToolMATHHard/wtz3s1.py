import math

def distance_point_to_line_3d_b(A, B, C):
    # |(C-A) x (B-A)| / |B-A|
    v=[B[i]-A[i] for i in range(3)]
    w=[C[i]-A[i] for i in range(3)]
    cx = w[1]*v[2] - w[2]*v[1]
    cy = w[2]*v[0] - w[0]*v[2]
    cz = w[0]*v[1] - w[1]*v[0]
    num = math.sqrt(cx*cx + cy*cy + cz*cz)
    den = math.sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2])
    return num/den
