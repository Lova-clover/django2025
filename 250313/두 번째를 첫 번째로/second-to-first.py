string = input()
arr = list(string)
a, b = arr[0], arr[1]

for i in range(len(arr)):
    if arr[i] == b:
        arr[i] = a

print("".join(arr))