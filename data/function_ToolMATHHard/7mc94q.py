def largest_common_arith_value(a1: int, d1: int, a2: int, d2: int, limit: int):
    """Return largest common value < limit."""
    vals=set()
    k=0
    while True:
        v=a1+d1*k
        if v>=limit:
            break
        vals.add(v)
        k+=1
    best=None
    m=0
    while True:
        v=a2+d2*m
        if v>=limit:
            break
        if v in vals:
            best=v
        m+=1
    return best
