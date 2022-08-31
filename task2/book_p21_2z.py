print('A B C F G')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = int(a and not (not c or not b) or not (not a or b) and c or a and c)
            g = int(a and c)
            print(a, b, c, f, g)