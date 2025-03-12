arr = [
 	input()
 	for _ in range(10)
]

a = input()
found = False

for i in range(10):
    if arr[i][len(arr[i])-1] == a:
        print(arr[i])
        found = True

if not found:
    print("None")