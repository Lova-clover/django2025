arr_cnt = [0] * 5
for _ in range(3):
    inp = input()
    arr = inp.split()
    a = arr[0]
    b = int(arr[1])

    if b>=37 and a=="Y":
        arr_cnt[0] += 1
    elif b>=37 and a=="N":
        arr_cnt[1] +=1
    elif b<37 and a=="Y":
        arr_cnt[2] +=1
    else:
        arr_cnt[3] +=1

for i in range(4):
    print(arr_cnt[i],end=" ")

if arr_cnt[0]>=2:
    print("E")
