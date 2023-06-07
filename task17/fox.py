*a, = map(int, open('17.txt'))
k = 0
for el in a:
    if abs(el) % 10 == 8:
        k += 1
b = []
for i in range(1, len(a)):
    p1, p2 = a[i - 1], a[i]
    if ((p1 < 0) or (p2 < 0)) and (p1 + p2)**2 >= k:
        b.append(p1 + p2)
print(len(b), max(b))