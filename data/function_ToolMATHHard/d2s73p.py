def count_numbers_with_two_digits():
    count=0
    for x in range(100,501):
        s=str(x)
        if s.count("3")>=2:
            count+=1
    return count
