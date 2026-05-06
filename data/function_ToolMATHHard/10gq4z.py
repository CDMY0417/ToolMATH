def smallest_crt_three_mods(m1,r1,m2,r2,m3,r3):
    """Brute-force smallest positive solution."""
    x=1
    while True:
        if x % m1 == r1 and x % m2 == r2 and x % m3 == r3:
            return x
        x+=1
