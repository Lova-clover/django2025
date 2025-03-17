n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.


arr = []
for elem in str:
    a = True
    for i in range(len(t)):
        if elem[i] != t[i]:
            a = False
            break
    if a:
        arr.append(elem)

arr.sort()

print(arr[k-1])