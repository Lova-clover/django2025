arr = list(map(int, input().split()))
arr_cnt = [0]*10

for elem in arr:
    if elem==0:
        break
    arr_cnt[elem//10] +=1

for i in range(1, 10):
    print(f"{i} - {arr_cnt[i]}")