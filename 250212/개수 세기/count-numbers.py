N, M = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if arr[i] == M:
        cnt+=1

print(cnt)