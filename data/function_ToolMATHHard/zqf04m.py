def reflection_from_image_pair(v1, v2, u):
    axis = [(v1[0]+v2[0])/2, (v1[1]+v2[1])/2]
    denom = axis[0]*axis[0] + axis[1]*axis[1]
    dot = u[0]*axis[0] + u[1]*axis[1]
    proj = [dot/denom*axis[0], dot/denom*axis[1]]
    return [2*proj[0]-u[0], 2*proj[1]-u[1]]
