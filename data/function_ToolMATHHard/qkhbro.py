def projection_matrix_chain(u, v):
    """Return matrix for projection onto u then onto v."""
    u1,u2=u; v1,v2=v
    # projection matrices
    uu = u1*u1+u2*u2
    vv = v1*v1+v2*v2
    Pu=[[u1*u1/uu, u1*u2/uu],[u1*u2/uu, u2*u2/uu]]
    Pv=[[v1*v1/vv, v1*v2/vv],[v1*v2/vv, v2*v2/vv]]
    # multiply Pv*Pu
    return [[Pv[0][0]*Pu[0][0]+Pv[0][1]*Pu[1][0], Pv[0][0]*Pu[0][1]+Pv[0][1]*Pu[1][1]],
            [Pv[1][0]*Pu[0][0]+Pv[1][1]*Pu[1][0], Pv[1][0]*Pu[0][1]+Pv[1][1]*Pu[1][1]]]
