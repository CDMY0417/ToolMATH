def intersection_point_of_lines_3d_a(p1, p2, q1, q2):
    'Find intersection point of lines through p1->p2 and q1->q2 in 3D.'
    v = [p2[i]-p1[i] for i in range(3)]
    w = [q2[i]-q1[i] for i in range(3)]
    a11, a12 = v[0], -w[0]
    a21, a22 = v[1], -w[1]
    b1 = q1[0]-p1[0]
    b2 = q1[1]-p1[1]
    det = a11*a22 - a12*a21
    if det == 0:
        a11, a12 = v[1], -w[1]
        a21, a22 = v[2], -w[2]
        b1 = q1[1]-p1[1]
        b2 = q1[2]-p1[2]
        det = a11*a22 - a12*a21
        if det == 0:
            raise ValueError('Lines are parallel or no unique intersection')
    t = (b1*a22 - b2*a12) / det
    return [p1[i] + t*v[i] for i in range(3)]
