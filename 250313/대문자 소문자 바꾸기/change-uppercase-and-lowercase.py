arr1 = input()
arr = list(arr1)

for i in range(len(arr)):
    if arr[i] >='a' and arr[i] <='z':
        arr[i] = chr(ord(arr[i])+ord('A')-ord('a'))
    else:
        arr[i] = chr(ord(arr[i])+ord('a')-ord('A'))

print("".join(arr))