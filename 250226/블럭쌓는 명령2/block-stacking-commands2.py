N, K = list(map(int, input().split()))
arr = [0] * N
max = 0

for _ in range(K):
    a, b = list(map(int, input().split()))
    while True:
        arr[a-1] +=1

        if a==b:
            break
        a+=1

for elem in arr:
    if elem > max:
        max = elem

print(max)

    
