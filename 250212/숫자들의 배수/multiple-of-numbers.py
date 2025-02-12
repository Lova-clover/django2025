n = int(input())
arr = []
cnt=1
cnt2=0

while True:
    arr.append(n*cnt)
    if arr[cnt-1]%5==0:
        cnt2+=1
    if cnt2>=2:
        break
    cnt+=1

for elem in arr:
    print(elem,end=" ")


