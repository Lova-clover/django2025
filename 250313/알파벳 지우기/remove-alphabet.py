arr1 = input()
arr2 = input()
string1 = ""
string2 = ""

for elem in arr1:
    if elem >= '0' and elem <='9':
        string1 += elem

for elem in arr2:
    if elem >= '0' and elem <='9':
        string2 += elem

print(int(string1)+int(string2))