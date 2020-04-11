for x in range(1, 9):
    for y in range(1, 9):
        for z in range(1, 9):
            if x + y + z == 10 and 9 * x + 5 * y + 2 * z == 61:
                print(x, y, z)
            else:
                continue
