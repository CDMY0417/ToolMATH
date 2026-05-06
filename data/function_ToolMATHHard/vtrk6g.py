def convert_base10_to_base5(value: int):
    if value == 0:
        return [0]
    digits=[]
    v=value
    while v>0:
        digits.append(v%5)
        v//=5
    return list(reversed(digits))
