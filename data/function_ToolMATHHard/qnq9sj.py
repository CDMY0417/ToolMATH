def reflection_point_on_plane_for_bounce(A, C, plane_normal, plane_d):
    # Reflect A across plane and intersect line with plane
    n = plane_normal
    n_dot_n = n[0]*n[0] + n[1]*n[1] + n[2]*n[2]
    if n_dot_n == 0:
        raise ValueError('plane_normal must be nonzero')
    factor = ((n[0]*A[0] + n[1]*A[1] + n[2]*A[2]) - plane_d) / n_dot_n
    D = [A[0] - 2*factor*n[0], A[1] - 2*factor*n[1], A[2] - 2*factor*n[2]]
    denom = n[0]*(C[0]-D[0]) + n[1]*(C[1]-D[1]) + n[2]*(C[2]-D[2])
    if denom == 0:
        raise ValueError('Line is parallel to plane')
    t = (plane_d - (n[0]*D[0] + n[1]*D[1] + n[2]*D[2])) / denom
    return [D[0] + t*(C[0]-D[0]), D[1] + t*(C[1]-D[1]), D[2] + t*(C[2]-D[2])]
