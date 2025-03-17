n = int(input())

# Please write your code here.
cnt= 0
def func(n):
    global cnt
    if n==1:
        return cnt
    
    if n%2==0:
        cnt+=1
        return func(n//2)
    else:
        cnt+=1
        returnfunc(n*3+1)
    
print(func(n))