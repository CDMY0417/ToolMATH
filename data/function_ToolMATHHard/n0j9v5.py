def base_conversion(value: int, base: int):
    # Convert integer value to list of digits in given base
    if value == 0:
        return [0]
    digits=[]
    v=value
    while v>0:
        digits.append(v%base)
        v//=base
    return list(reversed(digits))
