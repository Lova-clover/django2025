arr = list(map(int, input().split()))
arr_cnt = [0] * 11

for elem in arr:
    if elem == 0:
        break
    arr_cnt[elem//10] +=1

for i in range(10, 0, -1):
    print(f"{i*10} - {arr_cnt[i]}")