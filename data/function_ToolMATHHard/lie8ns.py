def u_n_special_sequence(n: int):
    """Return u_n for the block sequence."""
    if n <= 0:
        raise ValueError("n must be positive.")
    seq=[]
    current=1
    k=1
    last=0
    while len(seq) < n:
        # numbers congruent to k mod 3 greater than last
        count=0
        x=last+1
        while count<k:
            if x % 3 == k % 3:
                seq.append(x)
                count+=1
                last=x
                if len(seq) == n:
                    return seq[-1]
            x+=1
        k+=1
    return seq[n-1]
