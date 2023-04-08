*a, = map(int, open('17.txt').read().split())

min5 = 10**10
for el in a:
    if 100 <= el < 1000 and el < min5 and el % 10 == 5:
        min5 = el

res = []
for p1, p2 in zip(a, a[1:]):
    if (100 <= p1 < 1000 and (100 > p2 or p2 >= 1000) and (p1 + p2) % min5 == 0 or
       100 <= p2 < 1000 and (100 > p1 or p1 >= 1000) and (p1 + p2) % min5 == 0):
        res.append(p1 + p2)
print(len(res), max(res))