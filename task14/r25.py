n = 49**7 + 7**21 - 7
p = 7
c = 0
while n > 0:
    if n % p == 0:
        c += 1
    n //= p
print(c)