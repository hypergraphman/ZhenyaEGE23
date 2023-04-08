with open('17-1.txt') as f:
    a = [int(x) for x in f.readlines()]
    res = []
    avg = sum(a) / len(a)
    for i in range(len(a) - 1):
        if a[i] > avg and a[i + 1] > avg and abs(a[i] + a[i + 1]) % 100 == 31:
            res.append(a[i] + a[i + 1])
print(len(res), max(res))