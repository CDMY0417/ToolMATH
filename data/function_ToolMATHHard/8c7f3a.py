def largest_weight_from_total_and_diff(total: float, diff: float):
    # For weights a,a,b with b-a=diff and 2a+b=total
    b = (total + 2*diff) / 3
    return b
