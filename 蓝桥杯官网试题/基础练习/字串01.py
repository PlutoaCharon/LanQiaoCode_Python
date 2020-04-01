'''
# 方法一
for i in range(32):
    print("{0:0>5}".format(format(i, 'b')))
'''

# 方法二
for i in range(32):
    print(format(i, 'b').zfill(5))