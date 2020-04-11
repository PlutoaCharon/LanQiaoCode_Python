ans = 0
for a in range(1, 10):
    for b in range(1, 10):
        if a != b:
            for c in range(1, 10):
                if a != c and b != c:
                    for d in range(1, 10):
                        if a != d and b != d and c != d:
                            for e in range(1, 10):
                                if a != e and b != e and c != e and d != e:
                                    for f in range(1, 10):
                                        if a != f and b != f and c != f and d != f and e != f:
                                            for j in range(1, 10):
                                                if a != j and b != j and c != j and d != j and e != j and f != j:
                                                    for h in range(1, 10):
                                                        if a != h and b != h and c != h and d != h and e != h and f != h and j != h:
                                                            for i in range(1, 10):
                                                                if a != i and b != i and c != i and d != i and e != i and f != i and j != i and h != i:
                                                                    if a + b + c + d == d + e + f + h and a + b + c + d == h + i + j + a:
                                                                        print(a, b, c, d, e, f, h, i, j)
                                                                        ans += 1
print(ans)