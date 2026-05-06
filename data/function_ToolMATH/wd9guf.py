def inverse_lookup_in_table(func_table: dict, value: int):
    for key, val in func_table.items():
        if val == value:
            return key
    return None
