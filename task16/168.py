from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 2:
        return n
    return n + f(n - 2)


for n in range(1, 2023):
    f(n)

print(f(2023) + f(2020))