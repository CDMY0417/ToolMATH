def sum_smallest_n_with_four_divisors(n: int):
    # Sum of smallest n positive integers with exactly four divisors
    def count_divisors(x):
        cnt=0
        for i in range(1,int(x**0.5)+1):
            if x%i==0:
                cnt += 2 if i*i!=x else 1
        return cnt
    vals=[]
    x=2
    while len(vals)<n:
        if count_divisors(x)==4:
            vals.append(x)
        x+=1
    return sum(vals)
