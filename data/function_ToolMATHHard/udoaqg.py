def reflection_matrix_squared(v):
    # Compute R^2 for reflection over line spanned by v
    # Reflection matrix R = 2 vv^T/(v·v) - I, so R^2 = I
    return [[1,0],[0,1]]
