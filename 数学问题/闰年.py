def is_leapyear(num):
    if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
        return True
    return False

if __name__ == '__main__':
    num = int(input())
    if is_leapyear(num):
        print('yes')
    else:
        print('no')