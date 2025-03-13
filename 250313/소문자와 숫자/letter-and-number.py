arr = input()
arr2 = ""

for elem in arr:
    if elem.isalpha() or elem.isdigit():
        arr2+=elem

print(arr2.lower())