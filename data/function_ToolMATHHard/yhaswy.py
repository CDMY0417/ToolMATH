def ratio_w_over_x(x_over_y: float, y_over_z: float, z_over_w: float):
    # Compute w/x from chained ratios
    return 1 / (x_over_y * y_over_z * z_over_w)
