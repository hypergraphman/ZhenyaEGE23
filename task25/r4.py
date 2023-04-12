def n_to_p(n, p):
    res = ''
    while n > 0:
        res = '0123456789ABCDEF'[n % p] + res
        n //= p
    return res

# print(n_to_p(194, 5))

from fnmatch import fnmatch

for i in range(1, 2023**3):
    if fnmatch(str(i), '*2*0'):
        n_3 = n_to_p(i, 3)
        n_7 = n_to_p(i, 7)
        if n_3 == n_3[::-1] and n_7 == n_7[::-1]:
            print(i, sum(map(int, n_to_p(i, 8))))