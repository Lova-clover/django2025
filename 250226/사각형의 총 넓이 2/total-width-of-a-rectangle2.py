N = int(input())
arr = [[0 for i in range(201)] for i in range(201)]

for _ in range(N):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1
    
cnt=0

for i in range(201):
    for j in range(201):
        if arr[i][j] == 1:
            cnt +=1

print(cnt)