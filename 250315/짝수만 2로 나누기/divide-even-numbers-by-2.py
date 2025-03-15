n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr2 = []

def even(arr):
    for elem in arr:
        if elem%2==0:
            arr2.append(elem/2)
        else:
            arr2.append(elem)
    return arr2


for elem in even(arr):
    print(f"{elem:.0f}",end=" ")