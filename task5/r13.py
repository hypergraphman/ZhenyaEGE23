def alg(n):
    step1 = f'{n:b}'
    step2 = step1 + str(step1.count('1') % 2)
    step3 = step2 + str(step2.count('1') % 2)
    return int(step3, 2)


print(alg(28)) # проверка, обязательна

i = 1
while alg(i) <= 77:
    i += 1
print(i)
