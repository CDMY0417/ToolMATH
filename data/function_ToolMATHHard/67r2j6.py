def reflect_vector_from_image_pair(v1, v2, u):
    # Reflect vector u across the line through origin that maps v1 to v2
    axis = [(v1[0]+v2[0])/2, (v1[1]+v2[1])/2]
    denom = axis[0]*axis[0] + axis[1]*axis[1]
    if denom == 0:
        raise ValueError('axis vector cannot be zero')
    dot = u[0]*axis[0] + u[1]*axis[1]
    proj = [dot/denom * axis[0], dot/denom * axis[1]]
    return [2*proj[0] - u[0], 2*proj[1] - u[1]]
