'''
2.将LANQIAO中的字母重新排列，可以得到不同的单词，如LANQIAO、AAILNOQ等，注意这7个字母都要被用上，单词不一定有具体的英文意义。
请问，总共能排列如多少个不同的单词。

'''


import itertools
array=['l','a','o','q','i','a','o']
i=0
pailie=list(itertools.permutations(array))
for x in pailie:
    for y in x:
        print(y,end=' ')
        i=i+1
    print(i)
