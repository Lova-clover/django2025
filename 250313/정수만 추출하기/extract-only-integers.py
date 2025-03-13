arr1, arr2 = input().split()

for i in range(len(arr1)):
    if not arr1[i].isdigit():
        a = arr1[:i]
        break

for i in range(len(arr2)):
    if not arr2[i].isdigit():
        b = arr2[:i]
        break

print(int(a)+int(b))