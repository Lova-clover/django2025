n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
max1 = 0
def func(n):
    global max1
    if n==0:
        return max1
    
    if arr[n-1] > max1:
        max1 = arr[n-1]
        return func(n-1)
    else:
        return func(n-1)

print(func(n))