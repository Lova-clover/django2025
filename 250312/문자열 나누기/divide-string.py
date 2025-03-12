n = int(input())
arr = input()
arr2 = ""

for elem in arr:
    if elem != " ":
        arr2 += elem
cnt = 0

for elem in arr2:
    cnt +=1
    if cnt==6:
        cnt -=5
        print()
    print(elem,end="")
    