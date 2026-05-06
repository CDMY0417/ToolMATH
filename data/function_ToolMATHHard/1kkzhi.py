def apply_projection_from_example(v, w, u):
    """Return projection of u onto line spanned by w."""
    v1,v2=v; w1,w2=w; u1,u2=u
    # projection onto w
    ww = w1*w1 + w2*w2
    dot = u1*w1 + u2*w2
    return [dot/ww*w1, dot/ww*w2]
