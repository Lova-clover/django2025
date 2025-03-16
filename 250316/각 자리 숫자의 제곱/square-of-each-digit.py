N = int(input())

# Please write your code here.

def func(N):
    if N<1:
        return N
    
    return func(N//10) + (N%10)*(N%10)

print(func(N))
