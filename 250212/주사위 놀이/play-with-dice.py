arr = list(map(int, input().split()))
arr_cnt = [0] * 6

for elem in arr:
    arr_cnt[elem-1] +=1
 
for i in range(6):
    print(f"{i+1} - {arr_cnt[i]}")