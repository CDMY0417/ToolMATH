def range_geometric_three_digit(dummy: int = 0):
    """Return largest minus smallest geometric 3-digit number."""
    nums=[]
    for a in range(1,10):
        for b in range(0,10):
            for c in range(0,10):
                if len({a,b,c})<3:
                    continue
                if b*b==a*c:
                    nums.append(100*a+10*b+c)
    return max(nums) - min(nums)
