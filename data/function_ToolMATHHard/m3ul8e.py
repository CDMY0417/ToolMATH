import math

def norm_from_triple_product_scalar(k):
    if k >= 0:
        raise ValueError('Expected negative scalar for nonzero vectors')
    return math.sqrt(-k)
