n = int(input())
arr = list(map(int, input().split()))
min_num = 100

for i in range(1, n):  
    diff = arr[i] - arr[i - 1] 
    if diff < min_num: 
        min_num = diff

print(min_num)
    
    
