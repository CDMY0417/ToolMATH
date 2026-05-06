def find_inverse(func_dict: dict, y: int):
    for x, fx in func_dict.items():
        if fx == y:
            return x
    return None
