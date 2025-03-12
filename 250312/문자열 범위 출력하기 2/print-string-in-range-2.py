arr = input()
n = int(input())

if n > len(arr):
    print(arr[::-1])
else:
    for i in range(len(arr)-1,len(arr)-n-1,-1):
        print(arr[i],end="")