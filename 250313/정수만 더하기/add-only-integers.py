arr = input()
cnt = 0
for elem in arr:
    if elem >= '0' and elem <= '9':
        cnt += int(elem)
print(cnt)