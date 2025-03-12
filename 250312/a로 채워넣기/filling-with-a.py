string = input()
arr = list(string)
arr[1] = 'a'
arr[len(arr)-2] = 'a'

print("".join(arr))