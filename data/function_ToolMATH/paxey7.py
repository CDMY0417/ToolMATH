def f_x(x: int) -> int:
    if x % 21 == 0:
        return x // 21
    elif x % 7 == 0:
        return 3 * x
    elif x % 3 == 0:
        return 7 * x
    else:
        return x + 3
