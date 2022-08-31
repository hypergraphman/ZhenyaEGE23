print('A B C F G')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = int(a or not (b and not c) or not (a <= (not (not b and c))))
            g = int(b <= (a or c))
            print(a, b, c, f, g)