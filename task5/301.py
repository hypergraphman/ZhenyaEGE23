def f(n):
    s1 = bin(n)[2:]
    if s1.count('1') % 2 == 0:
        s2 = '10' + s1[2:] + '0'
    else:
        s2 = '11' + s1[2:] + '1'
    return int(s2, 2)


print(f(6))
print(f(4))

i = 1
while f(i) <= 40:
    i += 1
print(i)