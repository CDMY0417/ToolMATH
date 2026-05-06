import math

def tetrahedron_volume(A,B,C,D):
    # |(B-A)·((C-A)x(D-A))|/6
    v=[B[i]-A[i] for i in range(3)]
    w=[C[i]-A[i] for i in range(3)]
    u=[D[i]-A[i] for i in range(3)]
    cx = w[1]*u[2]-w[2]*u[1]
    cy = w[2]*u[0]-w[0]*u[2]
    cz = w[0]*u[1]-w[1]*u[0]
    dot = v[0]*cx+v[1]*cy+v[2]*cz
    return abs(dot)/6
