n = int(input())
arr = list(map(int, input().split()))
min_val = arr[0]
cnt=0

for elem in arr:
    if elem <= min_val:
        min_val = elem

for elem in arr:
    if elem==min_val:
        cnt +=1

print(min_val,cnt)