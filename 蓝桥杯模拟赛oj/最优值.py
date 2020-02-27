def main():
    n = int(input())
    ans = 0
    anslist = []
    for i in range(n):
        word = input()
        len_word = len(word)
        anslist.append(((ord(word[0])-96))*len_word)
    anslist = sorted(anslist)
    for i in range(n):
        ans += anslist[i]*(i+1)
    print(ans)
if __name__ == '__main__':
    main()
