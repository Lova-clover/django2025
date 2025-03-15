A = input()

# Please write your code here.

def alpa(A):
    for i in range(len(A)):
        cnt = 0
        for j in range(i+1, len(A)):
            if A[i] != A[j]:
                cnt+=1
        if cnt>=1:
            return True
    return False

if alpa(A):
    print("Yes")
else:
    print("No")

