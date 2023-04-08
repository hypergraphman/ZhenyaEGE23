*a, = map(int, open('17-205.txt').read().split())

res = []
for p1, p2 in zip(a, a[1:]):
    if (abs(p1) % 100 == 17 or abs(p2) % 100 == 17) and (p1 + p2) % 2 == 0:
        res.append(p1 + p2)
print(len(res), max(res))