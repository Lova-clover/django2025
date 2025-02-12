arr = list(map(int,input().split()))
arr2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    arr2[0] = arr[0]
    arr2[1] = arr[1]
    arr2[i+2] = arr2[i] + arr2[i+1]
    if arr2[i+2] >= 10:
        arr2[i+2] = arr2[i+2]%10
    print(arr2[i],end=" ")
