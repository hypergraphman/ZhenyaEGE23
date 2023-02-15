from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    if n > 1:
        return n * f(n - 1)

for i in range(1, 500):
    f(i)
print(f(500))