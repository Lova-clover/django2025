arr = list(map(int, input().split()))
arr2 = []
cnt=0

for i in range(100):
    if arr[i] == 0:
        break
    arr2.append(arr[i])
    cnt +=1
    
for i in range(cnt):
    if arr2[i]%2==0:
        print(arr2[i]//2,end=" ")
    else:
        print(arr2[i]+3,end=" ")