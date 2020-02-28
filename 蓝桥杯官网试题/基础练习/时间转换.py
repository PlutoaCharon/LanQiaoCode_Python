time = int(input())
hour = time // 3600
minute = (time - hour*3600) // 60
second = (time - hour*3600 - minute*60) % 60

print(hour,':',minute,':',second, sep='')