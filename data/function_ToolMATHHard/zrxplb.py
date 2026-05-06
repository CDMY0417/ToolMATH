import math

def rotate_vector_90deg_through_x_axis(v):
    'Rotate a 3D vector by 90 degrees in the plane through the x-axis.'
    if len(v) != 3:
        raise ValueError('v must have length 3')
    x, y, z = v
    r = math.sqrt(y*y + z*z)
    if r == 0:
        return [x, 0.0, 0.0]
    s = 1.0 if x >= 0 else -1.0
    return [
        s * r,
        -s * x * y / r,
        -s * x * z / r,
    ]
