N = int(input())
arr = [0 for i in range(100)]

for _ in range(N):
    x1, x2 = list(map(int, input().split()))
    while True:
        arr[x1] += 1
        if x1==x2:
            break
        x1+=1

max1 = 0

for elem in arr:
    if elem > max1:
        max1 = elem

print(max1)