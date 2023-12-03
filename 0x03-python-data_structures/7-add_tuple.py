def add_tuple(tuple_a=(), tuple_b=()):
    w, x, y, z = (0, 0, len(tuple_a), len(tuple_b))
    if y > 0:
        w = tuple_a[0]
    if z > 0:
        w += tuple_b[0]
    if y > 1:
        x = tuple_a[1]
    if z > 1:
        x += tuple_b[1]
    return (w, x)
