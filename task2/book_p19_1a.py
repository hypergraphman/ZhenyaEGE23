print('A B F')
for a in 0, 1:
    for b in 0, 1:
        f = int(not (a and b) or a and b)
        print(a, b, f)