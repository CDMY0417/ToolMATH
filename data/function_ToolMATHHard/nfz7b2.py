import math

def radius_circle_two_points_center_xaxis(p1, p2):
    # Circle center (h,0) equidistant to p1 and p2
    x1,y1 = p1
    x2,y2 = p2
    if x1 == x2:
        h = x1
    else:
        h = (x2**2 + y2**2 - x1**2 - y1**2) / (2*(x2 - x1))
    r = math.sqrt((x1 - h)**2 + y1**2)
    return r
