from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2) - 1
    if n > 0 and n % 2 != 0:
        return f(n - 1) + 1

s = set()
for i in range(0, 1000):
    if f(i) == 0:
        s.add(i)
print(len(s))