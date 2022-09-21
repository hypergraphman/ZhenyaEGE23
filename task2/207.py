print('a b c d')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = int((not (b <= a) and (c <= d)) != (a and b and c and not d))
                if f:
                    print(a, b, c, d)
