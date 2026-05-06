def prime_with_largest_gcd_exponent(exp1, exp2):
    # Return prime with largest exponent in gcd
    max_p=None
    max_e=-1
    for p in exp1:
        e=min(exp1[p], exp2.get(p,0))
        if e > max_e:
            max_e=e
            max_p=p
    return max_p
