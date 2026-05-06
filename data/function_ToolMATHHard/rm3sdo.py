def count_bad_times_mod4():
    count=0
    for x in range(160,200):
        if x%4==3:
            count+=1
    return count
