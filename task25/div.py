def divs(n):
    res = {1, n}
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)


print(divs(100), len(divs(100)) > 30)