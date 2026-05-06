def vector_triple_product(u: list[float], v: list[float], w: list[float]) -> list[float]:
    uvw = [(u[i] * w[i] for i in range(len(u)))]
    uv = [(u[i] * v[i] for i in range(len(u)))]
    first = [sum(j*w[j] for j in range(len(w))) * v[i] for i in range(len(v))]
    second = [sum(j*v[j] for j in range(len(v))) * w[i] for i in range(len(w))]
    return [first[i] - second[i] for i in range(len(u))]
