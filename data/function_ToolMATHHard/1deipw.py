from fractions import Fraction

def rational_roots(coeffs):
    # Find rational roots of integer polynomial using Rational Root Theorem
    def factors(n):
        n=abs(int(n))
        fac=set()
        for i in range(1, n+1):
            if n % i == 0:
                fac.add(i)
        return fac
    a0=coeffs[0]
    an=coeffs[-1]
    nums=factors(a0)
    dens=factors(an)
    roots=set()
    for p in nums:
        for q in dens:
            for s in (1,-1):
                r=Fraction(s*p, q)
                val=Fraction(0,1)
                for c in reversed(coeffs):
                    val = val*r + c
                if val == 0:
                    roots.add(r)
    return [float(r) for r in sorted(roots)]
