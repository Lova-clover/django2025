N = int(input())

# Please write your code here.

def func(N):
    if N==1:
        return 2
    if N==2:
        return 4
    
    return func(N-1)* func(N-2)

print(func(N)%100)