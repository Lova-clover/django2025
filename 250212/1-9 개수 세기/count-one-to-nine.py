n = int(input())
arr_cnt = [0]*9

arr = list(map(int, input().split()))
for elem in arr:
    arr_cnt[elem-1] +=1

for i in range(9):
    print(arr_cnt[i])