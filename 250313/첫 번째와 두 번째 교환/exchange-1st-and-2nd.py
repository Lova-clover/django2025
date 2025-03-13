string = input()
a = string[0]
b = string[1]
arr = list(string)

for i in range(len(arr)):
    if a == arr[i]:
        arr[i] = b
    elif b == arr[i]:
        arr[i] = a
print("".join(arr))


