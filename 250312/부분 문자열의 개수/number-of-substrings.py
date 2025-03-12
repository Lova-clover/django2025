string = input()
arr = input()
cnt = 0

for i in range(len(string)-1):
    if string[i] == arr[0] and string[i+1] == arr[1]:
        cnt +=1

print(cnt)