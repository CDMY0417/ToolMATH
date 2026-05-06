def csc_plus_cot_from_sec_plus_tan(sec_plus_tan: float):
    s = sec_plus_tan
    sec = (s + 1/s)/2
    tan = (s - 1/s)/2
    sin = tan / sec
    cos = 1/sec
    return (1 + cos)/sin
