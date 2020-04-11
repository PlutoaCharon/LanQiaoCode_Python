for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            numAB = int(str(a) + str(b))
            numBC = int(str(b) + str(c))
            if a + numAB == numBC:
                print(a, b, c)
