n = int(input())
arr = [0] * 200

for _ in range(n):
    a, b = list(map(int, input().split()))
    while True:
        if a==b:
            break
        arr[a] +=1
        a+=1

max1 = 0

for elem in arr:
    if elem > max1:
        max1 = elem
print(max1)
    





