import math

def cross_of_linear_combos(u_coeffs, v_coeffs, cross_ab, cross_ac, cross_bc):
    ua, ub, uc = u_coeffs
    va, vb, vc = v_coeffs
    axb = cross_ab
    axc = cross_ac
    bxc = cross_bc
    # u x v = ua*vb*(a x b) + ua*vc*(a x c) + ub*va*(b x a) + ub*vc*(b x c) + uc*va*(c x a) + uc*vb*(c x b)
    def vec_scale(s, v):
        return [s*vi for vi in v]
    def vec_add(x, y):
        return [xi+yi for xi,yi in zip(x,y)]
    res = [0.0, 0.0, 0.0]
    res = vec_add(res, vec_scale(ua*vb, axb))
    res = vec_add(res, vec_scale(ua*vc, axc))
    res = vec_add(res, vec_scale(ub*va, [-v for v in axb]))
    res = vec_add(res, vec_scale(ub*vc, bxc))
    res = vec_add(res, vec_scale(uc*va, [-v for v in axc]))
    res = vec_add(res, vec_scale(uc*vb, [-v for v in bxc]))
    # convert -0.0 to 0.0
    res = [0.0 if abs(v) < 1e-12 else v for v in res]
    return [int(v) if abs(v-round(v))<1e-9 else v for v in res]
