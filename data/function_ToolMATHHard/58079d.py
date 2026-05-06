def min_quadratic_form_3d(A, b, c: float):
    # Minimize x^T A x + b^T x + c for symmetric A
    a11,a12,a13 = A[0]
    a21,a22,a23 = A[1]
    a31,a32,a33 = A[2]
    M = [
        [2*a11,2*a12,2*a13],
        [2*a21,2*a22,2*a23],
        [2*a31,2*a32,2*a33],
    ]
    def det3(m):
        return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
              - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
              + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
    D = det3(M)
    if D == 0:
        raise ValueError('singular')
    def det_replace(col, vec):
        m = [row[:] for row in M]
        for i in range(3):
            m[i][col] = vec[i]
        return det3(m)
    bx = [-b[0], -b[1], -b[2]]
    x = det_replace(0, bx)/D
    y = det_replace(1, bx)/D
    z = det_replace(2, bx)/D
    val = 0
    v=[x,y,z]
    for i in range(3):
        for j in range(3):
            val += v[i]*A[i][j]*v[j]
    val += b[0]*x + b[1]*y + b[2]*z + c
    return val
