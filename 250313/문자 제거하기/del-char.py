string = input()
arr = list(string)

while True:
    n = int(input())
    if len(arr) < n:
        arr.pop(len(arr)-1)
    else:
        arr.pop(n)
    print("".join(arr))
    if len(arr) == 1:
        break


    
