n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr2 = []
def median(arr):
    for i in range(len(arr)):
        arr2.append(arr[i])
        if i%2==0:
            arr2.sort()
            print(arr2[i//2],end=" ")

median(arr)

            