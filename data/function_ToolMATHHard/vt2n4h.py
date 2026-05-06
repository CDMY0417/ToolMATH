def orthogonal_projection_other_component(v, proj_a):
    # For orthogonal components, proj_b = v - proj_a
    return [v[0] - proj_a[0], v[1] - proj_a[1]]
