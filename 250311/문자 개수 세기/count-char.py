arr = input()
alpa = input()

cnt= 0
for i in range(len(arr)):
    if alpa == arr[i]:
        cnt +=1

print(cnt)