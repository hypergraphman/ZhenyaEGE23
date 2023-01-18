s = 247 * '5'
while '222' in s or '555' in s:
    if '222' in s:
        s = s.replace('222', '5', 1)
    else:
        s = s.replace('555', '2', 1)
print(s)