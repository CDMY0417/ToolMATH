def base_n_to_base10(digits, base: int):
    val=0
    for d in digits:
        val = val*base + d
    return val
