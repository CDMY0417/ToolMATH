def compute_p6_from_p1_p5(p1: int, p5: int):
    # Find p(6) for nonnegative integer-coefficient polynomial, degree<=3
    for a0 in range(p1+1):
        for a1 in range(p1+1):
            for a2 in range(p1+1):
                for a3 in range(p1+1):
                    if a0+a1+a2+a3!=p1:
                        continue
                    if a0 + a1*5 + a2*25 + a3*125 == p5:
                        return a0 + a1*6 + a2*36 + a3*216
    raise ValueError('no solution')
