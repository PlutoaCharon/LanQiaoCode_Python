h, m = map(int, input().split())

time = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
        23: 'twenty three', 30: 'thirty', 40: 'forty', 50: 'fifty'}

if m == 0:
    print(time[h] + ' o\'clock')
else:
    print(time[h], end=' ')
    if 0 < m <= 20 or m == 30 or m == 40 or m == 50:
        print(time[m])
    elif 20 < m < 30:
        print(time[20] + ' ' + time[m - 20])
    elif 30 < m < 40:
        print(time[30] + ' ' + time[m - 30])
    elif 40 < m < 50:
        print(time[40] + ' ' + time[m - 40])
    else:
        print(time[50] + ' ' + time[m - 50])