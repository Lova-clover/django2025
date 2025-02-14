arr = list(map(int, input().split()))

max_num = 0
min_num = 1000

for elem in arr:
    if elem < 500 and elem > max_num:
        max_num = elem
    if elem > 500 and elem < min_num:
        min_num = elem

print(max_num, min_num)