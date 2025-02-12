a,b = map(int, input().split())

arr_cnt = [0]*10
arr_sum = 0
while True:
    arr_cnt[a%b] +=1
    a = a//b
    if a<=1:
        break

for elem in arr_cnt:
    arr_sum += elem * elem

print(arr_sum)