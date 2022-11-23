def alg(n):
    d1 = n // 100
    d2 = n // 10 % 10
    d3 = n % 10
    a = [d1 * 10 + d2, d2 * 10 + d1,
         d1 * 10 + d3, d3 * 10 + d1,
         d2 * 10 + d3, d3 * 10 + d2]
    mx = 0
    mn = 100
    for el in a:
        if 10 <= el <= 99:
            mx = max(el, mx)
            mn = min(el, mn)
    return mx - mn


from itertools import permutations
def alg2(n):
    a = list(map(lambda x: int(''.join(x)), filter(lambda x: 10 <= int(''.join(x)) <= 99, permutations(str(n), r=2))))
    return max(a) - min(a)


print(alg2(351))
i = 100
while alg2(i) != 40:
    i += 1
print(i)
