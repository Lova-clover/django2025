N = int(input())

# Please write your code here.

def fibo(N):
    if N==1:
        return 1
    if N==2:
        return 1
    
    return fibo(N-1) + fibo(N-2)

print(fibo(N))