print('A B C F')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = int(a and not b or b and not c or c and not a)
            print(a, b, c, f)