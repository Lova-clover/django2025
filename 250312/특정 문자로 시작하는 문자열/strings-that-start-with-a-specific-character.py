n = int(input())
arr = [
    input()
    for _ in range(n)
]
a = input()

cnt = 0
sum_cnt = ""


for i in range(n):
    if arr[i][0] == a:
        cnt +=1
        sum_cnt += arr[i]

print(f"{cnt} {len(sum_cnt)/cnt:.2f}")