n = int(input())
arr = list(map(int, input().split()))
max_val = 0
cnt = 0

for elem in arr:
    if elem > max_val:
        max_val = elem
    
for elem in arr:
    if elem == max_val:
        cnt+=1

if cnt>=2:
    print(-1)
else:
    print(max_val)