for a in range(0, 1000):
    if all(150 != y + 2 * x + 2 * z or a < x or a < y or a < z for x in range(1, 100) for y in range(1, 100) for z in range(1, 100)):
        print(a)