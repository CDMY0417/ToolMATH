import math

def orthogonal_component_from_projection(v, proj_a):
    if len(v) != len(proj_a):
        raise ValueError('Dimension mismatch')
    return [vi - pi for vi, pi in zip(v, proj_a)]
