def sum_roots_sum_reciprocals(points, k: float):
    # Solve sum 1/(x-a_i) = k, return sum of roots
    coeffs=[1.0]
    for a in points:
        new=[0.0]*(len(coeffs)+1)
        for i,c in enumerate(coeffs):
            new[i] += -a*c
            new[i+1] += c
        coeffs=new
    total=[0.0]*(len(coeffs)-1)
    for a in points:
        out=[0.0]*(len(coeffs)-1)
        out[-1]=coeffs[-1]
        for j in range(len(coeffs)-2,0,-1):
            out[j-1]=coeffs[j]+a*out[j]
        total=[total[i]+out[i] for i in range(len(out))]
    poly=[0.0]*len(coeffs)
    for i in range(len(coeffs)):
        t = total[i] if i < len(total) else 0.0
        poly[i]=t - k*coeffs[i]
    return -poly[-2]/poly[-1]
