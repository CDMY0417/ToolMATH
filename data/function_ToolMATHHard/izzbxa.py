def point_on_extended_segment(ratio_ap: float, ratio_pb: float):
    # P beyond A so t = -ratio_ap/(ratio_pb - ratio_ap)
    t = -ratio_ap/(ratio_pb - ratio_ap)
    u = 1 - t
    return [t, u]
