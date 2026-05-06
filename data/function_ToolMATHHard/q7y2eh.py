def remainder_quadratic_from_constraints(x0: float, r0: float, x1: float, r1: float, r1prime: float):
    # Quadratic r(x)=ax^2+bx+c with r(x0)=r0, r(x1)=r1, r'(x1)=r1prime
    A = [
        [x0*x0, x0, 1],
        [x1*x1, x1, 1],
        [2*x1, 1, 0],
    ]
    B = [r0, r1, r1prime]
    def det3(m):
        return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
              - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
              + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
    D = det3(A)
    if D == 0:
        raise ValueError('singular')
    def det_replace(col, vec):
        m = [row[:] for row in A]
        for i in range(3):
            m[i][col] = vec[i]
        return det3(m)
    a = det_replace(0,B)/D
    b = det_replace(1,B)/D
    c = det_replace(2,B)/D
    return [a,b,c]
