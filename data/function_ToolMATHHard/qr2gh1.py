def collinear_angle_bisector_vector(a, b):
    t = 13/8
    return [a[0] + t*(b[0]-a[0]), a[1] + t*(b[1]-a[1])]
