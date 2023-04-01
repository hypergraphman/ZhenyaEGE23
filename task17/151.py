*a, = map(int, open('17-1.txt').read().split())
res = []
for p1, p2, in zip(a, a[1:]):
    if str(p1)[-1] == '6' and p1 % 3 == 0 or abs(p2) % 10 == 6 and p2 % 3 == 0:
        res.append(min(p1, p2))
print(len(res), min(res))