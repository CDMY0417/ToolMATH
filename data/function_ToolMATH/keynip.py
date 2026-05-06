def inverse_lookup(f_dict: dict, value: int):
    for key, val in f_dict.items():
        if val == value:
            return key
    return None
