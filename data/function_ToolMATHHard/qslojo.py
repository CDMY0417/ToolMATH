def iterate_mobius_n_times(a: float, b: float, c: float, d: float, x: float, n: int):
    """Return f_n(x) for Mobius transform f(x)=(a x + b)/(c x + d)."""
    def mat_mul(X,Y):
        return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]],
                [X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]
    def mat_pow(M,n):
        R=[[1,0],[0,1]]
        B=M
        while n>0:
            if n&1:
                R=mat_mul(R,B)
            B=mat_mul(B,B)
            n//=2
        return R
    M=mat_pow([[a,b],[c,d]], n)
    A,B = M[0]
    C,D = M[1]
    denom = C*x + D
    if denom == 0:
        raise ValueError("Denominator zero.")
    return (A*x + B)/denom
