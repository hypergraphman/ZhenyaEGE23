from fnmatch import fnmatch


def divs(n):
    res = {1, n}
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)


for i in range(53, 10**7, 53):
    t = str(i)
    if fnmatch(t, '*2?2*') and t == t[::-1] and len(divs(i)) > 30:
        print(i, sum(divs(i)))
