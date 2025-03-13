n, A = input().split()
n = int(n)
cnt = 0
for _ in range(n):
    arr = input()
    if arr==A:
        cnt +=1

print(cnt)