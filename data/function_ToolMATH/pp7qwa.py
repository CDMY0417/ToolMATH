def identify_conic_section(coef_x2: float, coef_y2: float):
    if coef_x2 == 0 or coef_y2 == 0:
        return 'P'
    elif coef_x2 == coef_y2:
        return 'C'
    elif (coef_x2 > 0 and coef_y2 > 0) or (coef_x2 < 0 and coef_y2 < 0):
        return 'E'
    elif (coef_x2 > 0 > coef_y2) or (coef_x2 < 0 < coef_y2):
        return 'H'
    else:
        return 'N'
