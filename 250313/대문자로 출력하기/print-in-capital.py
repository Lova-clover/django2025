arr = input()
arr2 = []
for elem in arr:
    if elem.isalpha():
        arr2.append(elem)

print("".join(arr2).upper())