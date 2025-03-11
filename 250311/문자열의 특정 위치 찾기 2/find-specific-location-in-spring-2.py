n = input()
arr = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0
for i in range(5):
    if arr[i][2]==n or arr[i][3]==n:
        print(arr[i])
        cnt+=1

print(cnt)

