import math

def angle_from_three_points(X, Y, Z):
    v1 = [X[i]-Y[i] for i in range(3)]
    v2 = [Z[i]-Y[i] for i in range(3)]
    dot = sum(v1[i]*v2[i] for i in range(3))
    n1 = math.sqrt(sum(v1[i]*v1[i] for i in range(3)))
    n2 = math.sqrt(sum(v2[i]*v2[i] for i in range(3)))
    cosv = max(-1.0, min(1.0, dot/(n1*n2)))
    return math.degrees(math.acos(cosv))
