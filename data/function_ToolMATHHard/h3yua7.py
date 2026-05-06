def compute_Q6_from_Q1_Q5(Q1: int, Q5: int):
    # Find Q(6) for polynomial with nonnegative integer coeffs, degree<=3
    for a0 in range(Q1+1):
        for a1 in range(Q1+1):
            for a2 in range(Q1+1):
                for a3 in range(Q1+1):
                    if a0+a1+a2+a3!=Q1:
                        continue
                    if a0 + a1*5 + a2*25 + a3*125 == Q5:
                        return a0 + a1*6 + a2*36 + a3*216
    raise ValueError('no solution')
