string = input()
arr = ""
s2 = string[len(string)-1]

for _ in range(len(string)-2):
    arr += string

if s2 in arr:
    print(arr.index(s2))
else:
    print("No")