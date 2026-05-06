def max_sum_roots_linear_combo(digits):
    # Maximize b + (a+c)/2 with distinct digits a,b,c
    ds=sorted(digits)
    b=ds[-1]
    a=ds[-2]
    c=ds[-3]
    return b + (a+c)/2
