def cross_product_magnitude_squared(vector_a: tuple, basis_vector: tuple):
    x, y, z = vector_a
    i, j, k = basis_vector
    cross_prod = (y*k - z*j, z*i - x*k, x*j - y*i)
    return cross_prod[0]**2 + cross_prod[1]**2 + cross_prod[2]**2
