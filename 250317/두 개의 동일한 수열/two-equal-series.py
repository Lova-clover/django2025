n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()
YesNO = True

for i in range(n):
    if A[i] != B[i]:
        YesNO = False
        break
    
if YesNO:
    print("Yes")
else:
    print("No")