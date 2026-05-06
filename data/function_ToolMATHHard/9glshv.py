def add_polynomials(coeffs1, coeffs2):
    """Return coefficients for p(x)+q(x)."""
    n=max(len(coeffs1), len(coeffs2))
    p=[0]*(n-len(coeffs1))+list(coeffs1)
    q=[0]*(n-len(coeffs2))+list(coeffs2)
    res=[a+b for a,b in zip(p,q)]
    while len(res)>1 and res[0]==0:
        res.pop(0)
    return res
