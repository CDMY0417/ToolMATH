def sign_of_product(n: int, a: int, b: int) -> str:
    if n > a:
        f1_sign = 1
    elif n == a:
        f1_sign = 0
    else:
        f1_sign = -1
    if n > -b:
        f2_sign = 1
    elif n == -b:
        f2_sign = 0
    else:
        f2_sign = -1
    product_sign = f1_sign * f2_sign
    if product_sign > 0:
        return 'positive'
    elif product_sign == 0:
        return 'zero'
    else:
        return 'negative'
