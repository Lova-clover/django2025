arr = input()
cnt=1
arr2 = []


for elem in arr:
    if cnt%2==0:
        arr2.append(elem)
    cnt +=1

print("".join(arr2[::-1]))