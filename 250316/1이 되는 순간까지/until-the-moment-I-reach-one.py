N = int(input())

# Please write your code here.
cnt=0
def func(N):
    global cnt
    if N==1:
        return cnt
    
    if N%2==0:
        cnt+=1
        return func(N//2)
    else:
        cnt+=1
        return func(N//3)
    
print(func(N))