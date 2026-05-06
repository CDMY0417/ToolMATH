def coeff_of_x3_product(poly1, poly2):
    # poly lists coefficients [c0, c1, c2, ...]
    k = 3
    total = 0
    for i, a in enumerate(poly1):
        j = k - i
        if 0 <= j < len(poly2):
            total += a * poly2[j]
    return total
