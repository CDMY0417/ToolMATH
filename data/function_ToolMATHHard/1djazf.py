def count_bad_times_mod4():
    # Good times 100-159; bad in 160-199. Count numbers ==3 mod 4 in 160-199.
    count=0
    for x in range(160,200):
        if x%4==3:
            count+=1
    return count
