def other_endpoint(midpoint: tuple, endpoint: tuple) -> tuple:
    x = 2 * midpoint[0] - endpoint[0]
    y = 2 * midpoint[1] - endpoint[1]
    return (x, y)
