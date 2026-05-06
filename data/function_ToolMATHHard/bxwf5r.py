def orthogonal_vector_with_fixed_component(u, v):
    ux,uy,uz = u; vx,vy,vz = v
    cx = uy*vz - uz*vy
    cy = uz*vx - ux*vz
    cz = ux*vy - uy*vx
    t = 1 / cy
    return [cx*t, cz*t]
