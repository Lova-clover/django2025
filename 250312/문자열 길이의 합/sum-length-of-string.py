n = int(input())
cnt = 0
cnt_a = 0

for _ in range(n):
    arr = input()
    if arr[0] == "a":
        cnt_a +=1
    cnt += len(arr)

print(cnt, cnt_a)
