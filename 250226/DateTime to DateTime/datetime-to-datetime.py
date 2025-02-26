A, B, C = list(map(int, input().split()))

time1 = 11*24*60 + 11*60 + 11
time2 = A*24*60 + B*60 + C

if time1>time2:
    print(-1)
else:
    time = time2 - time1
    print(time)





