def piecewise_f0(x: int) -> int:
    if x < -100:
        return x + 200
    elif -100 <= x < 100:
        return -x
    else:
        return x - 200
