def f(n):
    if n < 10:
        return n
    return f(g(n))


def g(n):
    if n < 10:
        return f(n)
    return g(n % 10) + g(n // 10)


k = 0
for n in range(1, 600):
    if f(n) == 3:
        k += 1
print(k)