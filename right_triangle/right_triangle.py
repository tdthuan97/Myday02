def right_triangle(a, b, c):
    tri = [a, b, c]
    tri.sort()
    if tri[0] ** 2 + tri[1] ** 2 == tri[2] ** 2:
        return True
    return False
