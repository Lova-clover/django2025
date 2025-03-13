A = input()
B = input()
cnt = 0
for _ in range(len(A)):
    A = A[1:] + A[:1]
    cnt +=1
    if A == B:
        break
if A==B:
    print(cnt)
else:
    print("-1")