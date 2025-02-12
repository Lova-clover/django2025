arr = list(map(int, input().split()))
arr2 = []
arr2.append(arr[0])
arr2.append(arr[1])

for i in range(2, 10):
    arr2.append(arr2[i-1]+(2*arr2[i-2]))

for elem in arr2:
    print(elem, end=" ")