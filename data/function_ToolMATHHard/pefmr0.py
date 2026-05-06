def point_from_scaled_function_graph(x_scaled: float, y_scaled: float, x_scale: float, y_scale: float):
    # Given point on y = y_scale * f(x_scale * x), return corresponding point on y=f(x)
    x = x_scale * x_scaled
    y = y_scaled / y_scale
    return [x, y]
