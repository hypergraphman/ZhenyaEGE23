def f(s, e):
    if s < e:
        return 0
    if s == e:
        return 1
    return f(s - 4, e) + f(s // 2, e)


print(f(74, 10) * f(10, 2))
