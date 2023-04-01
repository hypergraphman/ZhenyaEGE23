*a, = map(int, open('17-1.txt').read().split())
res = []
for p1, p2, in zip(a, a[1:]):
    if p1 % 7 == 0 and p2 % 17 != 0 or p1 % 17 != 0 and p2 % 7 == 0:
        res.append(p1 + p2)
print(len(res), min(res))