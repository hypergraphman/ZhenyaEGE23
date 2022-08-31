print('A B C F')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = int(a and (not b and not c or b and c) or a and (b and not c or not b and c))
            print(a, b, c, f)