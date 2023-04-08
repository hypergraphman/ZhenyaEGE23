*a, = map(int, open('17-1.txt').read().split())

avg = sum(a) / len(a)
res = []
for p1, p2, in zip(a, a[1:]):
    if p1 > avg and p2 > avg and abs(p1 + p2) % 100 == 31:
        res.append(p1 + p2)
print(len(res), max(res))