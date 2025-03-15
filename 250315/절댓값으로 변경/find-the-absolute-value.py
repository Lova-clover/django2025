n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def abs1(arr):
    for i in range(n):
        arr[i] = abs(arr[i])

abs1(arr)
for elem in arr:
    print(elem, end=" ")
