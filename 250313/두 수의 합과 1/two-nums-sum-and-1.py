a, b = list(map(int, input().split()))

c = str(a+b)
cnt = 0
for elem in c:
    if elem=="1":
        cnt +=1

print(cnt)