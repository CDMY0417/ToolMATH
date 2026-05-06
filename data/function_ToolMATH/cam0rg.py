def distributed_power_of_product(coeff: int, var_exp: tuple, exp: int) -> tuple:
    coeff_result = coeff ** exp
    var, var_exp_base = var_exp
    var_exp_result = var_exp_base * exp
    return coeff_result, (var, var_exp_result)
