*a, = map(int, open('17-282.txt').read().split())

min17 = 10**10
for el in a:
    if el % 17 == 0 and el < min17:
        min17 = el

# min17 = min(filter(lambda x: x % 17 == 0, a))

res = []
for i in range(len(a) - 1):
    p1, p2 = a[i], a[i + 1]
# for p1, p2 in zip(a, a[1:]):
    if p1 % min17 == 0 or p2 % min17 == 0:
        res.append(p1 + p2)
print(len(res), max(res))


def sum_digit(n):
    res = 0
    while n > 0:
        res += n % 8
        n //= 8
    return res
print(sum_digit(1234))

# sum(map(int, str(1234)))
# print(sum(map(int, str(1234))))
count, mn = 0, float('inf')
