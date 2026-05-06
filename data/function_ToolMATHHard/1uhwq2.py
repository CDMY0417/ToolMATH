from fractions import Fraction

def count_possible_rational_roots(a: int, c: int):
    """Return count of distinct possible rational roots by rational root theorem."""
    ps=[]
    for p in range(1, abs(c)+1):
        if c % p == 0:
            ps.append(p)
    qs=[]
    for q in range(1, abs(a)+1):
        if a % q == 0:
            qs.append(q)
    vals=set()
    for p in ps:
        for q in qs:
            vals.add(Fraction(p,q))
            vals.add(Fraction(-p,q))
    return len(vals)
