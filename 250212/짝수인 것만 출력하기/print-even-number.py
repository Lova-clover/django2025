n = int(input())
arr = list(map(int, input().split()))
arr2 = []

for i in range(n):
    if arr[i]%2==0:
        arr2.append(arr[i])


for elem in arr2:
    print(elem, end=" ")