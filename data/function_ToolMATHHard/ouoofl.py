def count_multiples_with_square_bound():
    count=0
    for x in range(-100,101):
        if x%6==0 and x*x<200:
            count+=1
    return count
