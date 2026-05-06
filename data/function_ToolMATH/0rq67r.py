def factor_out_squares(product: int):
    squares = 1
    non_square = product
    factor = 2
    while factor * factor <= non_square:
        count = 0
        while non_square % factor == 0:
            non_square //= factor
            count += 1
        if count > 0:
            squares *= factor ** (count // 2)
            if count % 2: 
                non_square *= factor
        factor += 1
    if non_square > 1:
        return squares, non_square
    return squares, 1
