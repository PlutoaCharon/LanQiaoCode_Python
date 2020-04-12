numerate : float = 4.0
denominator : float = 1.0
operation : float = 1.0
PI = 0
for i in range(1, 2021):
    PI += operation * (numerate / denominator)
    denominator += 2
    operation *= -1
print('%.6f' % PI)
