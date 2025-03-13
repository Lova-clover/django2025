cnt = 0 
arr2 = ""
while True:
    arr = input()
    if arr=="0":
        break
    cnt +=1
    if cnt%2==1:
        arr2 += arr +"\n"

print(cnt)
print(arr2)

    