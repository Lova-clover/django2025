n = int(input())
arr = list(map(int, input().split()))
num = [0] * n
min_num = 100

for i in range(n):
    if i==0:
        num[0] = arr[0]
    else:
        num[i] = arr[i] - arr[i-1]

for i in range(n):
    if num[i] < min_num:
        min_num = num[i]

print(min_num)
    
    
