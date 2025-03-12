string = input()
arr = ""
s2 = string[len(string)-1]

for i in range(len(string)-2):
    arr += string[i]

if s2 in arr:
    print(arr.index(s2))
else:
    print("No")